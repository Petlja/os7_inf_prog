pythonInitialized = false;

SIM_STATUS_STOPPED = 1
SIM_STATUS_PLAYING = 2
SIM_STATUS_PAUSED = 3
SIM_STATUS_FINISHED = 4

simanimList = {}
pyodideCodeList = {}

function SimAnim (opts) {
    if (opts) {
        this.init(opts);
    }
}

SimAnim.prototype.init = async function(opts){
	this.opts = opts
	this.id = opts.id
	this.simStatus = SIM_STATUS_STOPPED
	this.code = popAttribute(opts,'data-code',"") 
	this.imgPath = popAttribute(opts,'data-img-path',"")
	this.scale = parseFloat(popAttribute(opts,'data-scale',"1"))
	this.originalScale = this.scale;
	this.pythonError = false
	this.pythonErrorMsg = ""
	this.varsInputElementId = {}
	this.eventQue = []
	this.simImages = {}
	this.drawFunctions = {'circle' : this.drawCircle,
						  'box' : this.drawBox,
						  'line' : this.drawLine, 
						  'triangle' : this.drawTriangle,
						  'polyLine' : this.drawPolyLine,
						  'image' : this.drawImage,
						  'text' : this.drawText,
						  'rotate' : this.rotate,
						  'restore' : this.restore
						}
	await this.execPython()
	if(this.pythonError){
	   console.log('Animation id: '+ this.id + '\nPython error:\n')
	   console.log(this.pythonErrorMsg)
	}
	else{
		this.generateHTMLForSim() 
		this.setupCanvas()
	}
}

SimAnim.prototype.execDrawing = async function(){
	for(var i =0; i < this.eventQue.length; i++){
		await this.eventQue[i]()
	}
	this.eventQue = []
}

SimAnim.prototype.rescale = function(){
	this.scale = this.originalScale
	var simWidth = this.animation_instance.anim_context.settings.window_with_px * this.scale;
	var mainContentWidth = document.getElementById('main-content').getBoundingClientRect().width - 50;
	if(simWidth >  mainContentWidth){
		this.scale = this.scale* parseFloat((mainContentWidth/simWidth).toFixed(2));
	}
	// settings	
	this.canvas.width = this.animation_instance.anim_context.settings.window_with_px * this.scale;
	this.canvas.height = this.animation_instance.anim_context.settings.window_height_px * this.scale;
	this.bufferCanvs.width = this.canvas.width;
	this.bufferCanvs.height = this.canvas.height;
	
	//we use this to scale all of the animations
	this.pixelPerUnit =  this.animation_instance.anim_context.settings.px_per_unit * this.scale;
}

SimAnim.prototype.setupCanvas = async function() {
	//creating buffer canvas	
	this.bufferCanvs =  document.createElement('canvas');
	this.bufferCanvsContext = this.bufferCanvs.getContext('2d');

	//adjust scale based on current windows size
	this.rescale()

	//settings
	this.animation_instance_x_min = this.animation_instance.anim_context.settings.view_box[0][0]
	this.animation_instance_y_min  =  this.animation_instance.anim_context.settings.view_box[0][1]
	this.animation_instance_height = this.animation_instance.anim_context.settings.view_box[2]
	this.frame_period = parseFloat(this.animation_instance.anim_context.settings.frame_period.toFixed(5))
	this.frameTime = this.frame_period * 1000;
	this.background_color =  this.animation_instance.anim_context.settings.background_color

	//drawing
	this.bufferCanvsContext.fillStyle = this.background_color
	this.bufferCanvsContext.fillRect(0, 0, this.bufferCanvs.width, this.bufferCanvs.height);
	this.animation_instance.queueFrame();
	await this.execDrawing()
	
	//swaping buffer with main canvas
	this.canvasContext.drawImage(this.bufferCanvs,0,0)	
}

SimAnim.prototype.setPythonErrorMsg = function(errMsg){
		this.pythonError = true
		this.pythonErrorMsg = errMsg
}

SimAnim.prototype.execPython = function(){
	pyodide.globals.the_script = this.code
	return pyodide.runPythonAsync(`
			try:
				exec(the_script,{'animation_instance_key' : '${this.id}'})
			except Exception:
				exc_type, exc_value, exc_tb = sys.exc_info()
				error_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb.tb_next))
				js.throwError(error_msg)
			else:
				import simanim.pyodide.gui	
			`)
		.then(() => {				
			this.animation_instance = pyodide.globals.simanim.pyodide.gui.animation_instance[this.id];
		})
		.catch((msg) => {this.setPythonErrorMsg(msg);})
}

SimAnim.prototype.generateHTMLForSim = function() {
	this.simDiv = document.createElement('div');
	this.simDiv.setAttribute('class', 'modal-sim');

	var simDivContent = document.createElement('div');
	simDivContent.setAttribute('class', 'modal-content-sim');

	var simDivControls = document.createElement('div');
	simDivControls.setAttribute('class', 'sim-controls');

	var controlBtnDiv = document.createElement('div');
	controlBtnDiv.setAttribute('class', 'control-button-div');

	this.playBtn = document.createElement('button');
	this.playBtn.setAttribute('class', 'control-btn');
	this.playBtn.addEventListener('click', this.startSim.bind(this));
	this.playBtn.innerHTML = '<i class="fas fa-play"></i> PLAY';

	this.stopBtn = document.createElement('button');
	this.stopBtn.setAttribute('class', 'control-btn');
	this.stopBtn.setAttribute('disabled', 'disabled');
	this.stopBtn.addEventListener('click', this.stopSim.bind(this));
	this.stopBtn.innerHTML = '<i class="fas fa-stop"></i> STOP';

	this.pauseBtn = document.createElement('button');
	this.pauseBtn.setAttribute('class', 'control-btn d-none');
	this.pauseBtn.addEventListener('click', this.pauseSim.bind(this));
	this.pauseBtn.innerHTML = '<i class="fas fa-pause"></i> PAUSE';

	controlBtnDiv.appendChild(this.playBtn);
	controlBtnDiv.appendChild(this.pauseBtn);
	controlBtnDiv.appendChild(this.stopBtn);
	
	simDivControls.appendChild(controlBtnDiv);

	var variablesDiv = document.createElement('div');
	variablesDiv.setAttribute('class', 'sim-modal-variables');
	variablesDiv.setAttribute('id', 'variablesDiv');

	var variables = this.animation_instance.getVars();
	for (var i = 0; i < variables.length; i++) {
		if (variables[i].meta["type"] == 'InputFloat') {
			var variableLabel = document.createElement('label');
			variableLabel.setAttribute('class', 'variable-label');
			variableLabel.innerHTML = `${variables[i].name} = `;

			var max = variables[i]['meta']['limit_to']
			var step = Math.pow(10,Math.floor(Math.log10(max)-1))

			var variableInput = document.createElement('input');
			variableInput.setAttribute('type', 'number');
			variableInput.setAttribute('class', 'variable-input');	
			variableInput.setAttribute('id', this.id + '-' +i)		
			variableInput.setAttribute('value', '' + variables[i]['meta']['default']);
			variableInput.setAttribute('min',variables[i]['meta']['limit_from'])
			variableInput.setAttribute('max',variables[i]['meta']['limit_to'])		
			variableInput.setAttribute('step', step);
			variableInput.addEventListener('input',this.setGetters.bind(this))

			this.varsInputElementId[variables[i].name] = this.id + '-' +i	

			variablesDiv.appendChild(variableLabel);
			variablesDiv.appendChild(variableInput);
		}
		else {
			var variableLabel = document.createElement('label');
			variableLabel.setAttribute('class', 'variable-label');
			variableLabel.innerHTML = `${variables[i].name} = `;

			var selectInput = document.createElement('select');
			selectInput.setAttribute('class', 'variable-input')
			selectInput.setAttribute('id', this.id + '-' +i)
			selectInput.addEventListener('input',this.setGetters.bind(this))

			for (var j = 0; j < variables[i].meta.lov.length; j++) {
				var selectOption = document.createElement('option');
				selectOption.innerHTML = variables[i].meta.lov[j];
				if(variables[i].meta.lov[j] == variables[i].meta.default){
					selectOption.setAttribute('selected','selected')	
				}
				selectInput.appendChild(selectOption);
			}
			this.varsInputElementId[variables[i].name] = this.id + '-' +i

			variablesDiv.appendChild(variableLabel);
			variablesDiv.appendChild(selectInput);
		}
	}

	if(variables.length > 0){
		simDivControls.appendChild(variablesDiv);
	}
	
	var simBodyCanvasDiv = document.createElement('div');
	simBodyCanvasDiv.setAttribute('class', 'sim-modal-canvas');

	this.canvas = document.createElement('canvas');
	this.canvas.setAttribute('id', 'simCanvas-' + this.id);
	this.canvas.setAttribute('class', ' sim-canvas')
	this.canvasContext = this.canvas.getContext('2d');

	simBodyCanvasDiv.appendChild(this.canvas);
	simDivContent.appendChild(simDivControls);
	simDivContent.appendChild(simBodyCanvasDiv);

	this.simDiv.appendChild(simDivContent);
	this.opts.appendChild(this.simDiv);
}

SimAnim.prototype.startSim = function() {
	this.playBtn.classList.add('d-none');
	this.pauseBtn.classList.remove('d-none');
	this.stopBtn.removeAttribute('disabled');

	for (var varName in this.varsInputElementId) {
		document.getElementById(this.varsInputElementId[varName]).setAttribute('disabled','true');
	}
	this.simStatus = SIM_STATUS_PLAYING;
	this.animationStart = window.performance.now();
	this.nextFrameTargetTime = window.performance.now();
	this.drawAnimation.call(this);
}

SimAnim.prototype.flipFrame = function(timestamp){
	// waite for the next animationFrame, interpolate in the meantime if we are close enough
	if(timestamp < this.nextFrameTargetTime + this.frameTime * 0.9){
		if((timestamp > this.nextFrameTargetTime + this.frameTime * 0.6)){
			if(this.canvasContext.globalAlpha !== 0.5){
				this.canvasContext.globalAlpha = 0.5;
				this.canvasContext.drawImage(this.bufferCanvs,0,0);
			}
			window.requestAnimationFrame((timestemp) => {this.flipFrame.call(this,timestemp);});
		}
		else{
			window.requestAnimationFrame((timestemp) => {this.flipFrame.call(this,timestemp);});
		}
	}
	else{
		this.canvasContext.globalAlpha = 1;
		this.canvasContext.drawImage(this.bufferCanvs,0,0);
		this.nextFrameTargetTime = timestamp;
		setTimeout(()=>{this.drawAnimation();},0);
	}
}

SimAnim.prototype.drawAnimation = function(){
	this.clearBufferCanvas();
	this.animation_instance.updateBetweenFrames();
	this.animation_instance.queueFrame();
	this.execDrawing();
	if (!this.animation_instance.getEndAnimation() && this.simStatus == SIM_STATUS_PLAYING) {
		window.requestAnimationFrame((timestemp) => {this.flipFrame.call(this,timestemp);});
	}
	else if (this.animation_instance.getEndAnimation()){
		//last buffered frame drawn
		setTimeout(()=>{this.canvasContext.drawImage(this.bufferCanvs,0,0);},this.frameTime);
		this.simStatus = SIM_STATUS_FINISHED;
		this.playBtn.classList.remove('d-none');
		this.playBtn.setAttribute('disabled', 'disabled');
		this.pauseBtn.classList.add('d-none');
		//console.log((window.performance.now() - this.animationStart)/1000);
	}
}

SimAnim.prototype.setGetters =async  function(){
	variableValues = {};
	for (var varName in this.varsInputElementId) {
		variableValues[varName] = this.varsInputElementId[varName]; 
	}
	
	// resets the animation to the begining
	this.animation_instance.setVarGetters(variableValues);

	this.clearBufferCanvas();
	this.animation_instance.queueFrame();

	await this.execDrawing();
	this.canvasContext.clearRect(0, 0, this.canvas.width, this.canvas.height);
	this.canvasContext.drawImage(this.bufferCanvs,0,0)

	// populate buffer
	this.animation_instance.updateBetweenFrames();
	this.animation_instance.queueFrame();
	this.execDrawing();
}

SimAnim.prototype.cleanUp =async function(){
	this.canvasContext.globalAlpha = 1;
	this.simStatus = SIM_STATUS_STOPPED
	this.eventQue = []
	this.animation_instance.resetAnimation();
	this.clearBufferCanvas();
	this.animation_instance.queueFrame();
	await this.execDrawing()

	//swap first frame to main canvas
	this.canvasContext.clearRect(0, 0, this.canvas.width, this.canvas.height);
	this.canvasContext.drawImage(this.bufferCanvs,0,0)

	this.playBtn.classList.remove('d-none');
	this.playBtn.removeAttribute('disabled');
	this.pauseBtn.classList.add('d-none');
	this.stopBtn.setAttribute('disabled', 'disabled');

	for (var varName in this.varsInputElementId) {
		document.getElementById(this.varsInputElementId[varName]).removeAttribute('disabled')
	}
}

SimAnim.prototype.stopSim = function() {
	this.cleanUp()
}

SimAnim.prototype.pauseSim = function() {
	this.playBtn.classList.remove('d-none');
	this.pauseBtn.classList.add('d-none');
	this.simStatus = SIM_STATUS_PAUSED
}

SimAnim.prototype.queueDrawEvent = function(type, obj){
	this.eventQue.push(this.drawFunctions[type].bind(this, obj))
}

SimAnim.prototype.clearBufferCanvas = function() {
	this.bufferCanvsContext.clearRect(0, 0, this.bufferCanvs.width, this.bufferCanvs.height);
	this.bufferCanvsContext.fillStyle = this.background_color
	this.bufferCanvsContext.fillRect(0, 0, this.bufferCanvs.width, this.bufferCanvs.height);
}

SimAnim.prototype.scalarToPixel = function(scalar){
	return scalar * this.pixelPerUnit
}

SimAnim.prototype.pointToPixel = function(point){
	var scalarPointX = this.scalarToPixel(point[0] - this.animation_instance_x_min)
	var scalarPointY = this.scalarToPixel(this.animation_instance_y_min + this.animation_instance_height - point[1])
	return [scalarPointX, scalarPointY]
}
SimAnim.prototype.rectToPixel = function(rect){
	var xy_min = this.pointToPixel([rect.xy_min[0],rect.xy_min[1] + rect.height])
	var width = this.scalarToPixel(rect.width)
	var height = this.scalarToPixel(rect.height)
	return [xy_min, width, height]
}

SimAnim.prototype.drawCircle = function(circle){
	this.bufferCanvsContext.save()
	this.bufferCanvsContext.strokeStyle = (circle.pen_color && circle.line_width) ? circle.pen_color : circle.fill_color
	this.bufferCanvsContext.lineWidth  = circle.line_width ?  this.scalarToPixel(circle.line_width)  : 1
	this.bufferCanvsContext.fillStyle = circle.fill_color; 
	if (this.bufferCanvsContext.line_dashed) {
		this.bufferCanvsContext.setLineDash([5, 5])
	}
	var center = this.pointToPixel(circle.center)
	var radius = this.scalarToPixel(circle.radius)
	this.bufferCanvsContext.beginPath();
	this.bufferCanvsContext.arc(center[0], center[1], radius, 0, 2 * Math.PI, false);
	this.bufferCanvsContext.closePath();
	this.bufferCanvsContext.fill();
	this.bufferCanvsContext.stroke();
	this.bufferCanvsContext.restore();
}

SimAnim.prototype.drawBox = function(rect) {
	this.bufferCanvsContext.save()
	this.bufferCanvsContext.lineWidth  = rect.line_width ?  this.scalarToPixel(rect.line_width)  : 1;
	this.bufferCanvsContext.strokeStyle = (rect.pen_color && rect.line_width) ? rect.pen_color : rect.fill_color;
	this.bufferCanvsContext.fillStyle = rect.fill_color;
	if (rect.line_dashed) {
		this.bufferCanvsContext.setLineDash([5, 5])
	}
	var scaledRect = this.rectToPixel(rect)
	this.bufferCanvsContext.beginPath();
	this.bufferCanvsContext.rect(scaledRect[0][0], scaledRect[0][1], scaledRect[1], scaledRect[2]);
	this.bufferCanvsContext.closePath();
	this.bufferCanvsContext.fill();
	this.bufferCanvsContext.stroke();

	this.bufferCanvsContext.restore()
}

SimAnim.prototype.drawLine = function(line) {
	this.bufferCanvsContext.save()
	this.bufferCanvsContext.strokeStyle = line.pen_color
	this.bufferCanvsContext.lineWidth = this.scalarToPixel(line.line_width);
	if (line.line_dashed) {
		this.bufferCanvsContext.setLineDash([5, 5])
	}
	this.bufferCanvsContext.beginPath();
	var point1 = this.pointToPixel(line.point1)
	var point2 = this.pointToPixel(line.point2)
	this.bufferCanvsContext.moveTo(point1[0], point1[1]);
	this.bufferCanvsContext.lineTo(point2[0], point2[1]);
	this.bufferCanvsContext.stroke();
	this.bufferCanvsContext.restore()
}
SimAnim.prototype.drawPolyLine = function(polyLine) {
	this.bufferCanvsContext.save()
	var numberOfPoints = polyLine.points.length
	if (numberOfPoints < 1) {
		return;
	}
	let points = polyLine.points
	this.bufferCanvsContext.strokeStyle = (polyLine.pen_color && polyLine.line_width) ? polyLine.pen_color : polyLine.fill_color;
	this.bufferCanvsContext.lineWidth =  polyLine.line_width ?  this.scalarToPixel(polyLine.line_width)  : 1;
	this.bufferCanvsContext.fillStyle = polyLine.fill_color;
	if (polyLine.line_dashed) {
		this.bufferCanvsContext.setLineDash([5, 5])
	}
	this.bufferCanvsContext.beginPath();
	var scalarPointX 
	var scalarPointY 
	[scalarPointX, scalarPointY] = this.pointToPixel(points[0])
	this.bufferCanvsContext.moveTo(scalarPointX,scalarPointY)
	for (i = 1; i < numberOfPoints; i++) {
		[scalarPointX, scalarPointY] = this.pointToPixel(points[i])
		this.bufferCanvsContext.lineTo(scalarPointX,scalarPointY)
	};
	this.bufferCanvsContext.stroke();
	this.bufferCanvsContext.restore()
}
//triangle[6] canvas settings
//trinagle[0] point 1  X
//trinagle[1] point 1  Y
//trinagle[2] point 2  X
//trinagle[3] point 2  Y
//trinagle[4] point 3  X
//trinagle[5] point 3  Y
SimAnim.prototype.drawTriangle = function(triangle) {
	this.bufferCanvsContext.save()
	this.bufferCanvsContext.strokeStyle = triangle[6].pen_color;
	this.bufferCanvsContext.lineWidth  = this.scalarToPixel(triangle[6].line_width);
	this.bufferCanvsContext.fillStyle = triangle[6].pen_color;
	if (triangle[6].line_dashed) {
		this.bufferCanvsContext.setLineDash([5, 5])
	}
	var point1 = this.pointToPixel([triangle[0],triangle[1]])
	var point2 = this.pointToPixel([triangle[2],triangle[3]])
	var point3 = this.pointToPixel([triangle[4],triangle[5]])
	this.bufferCanvsContext.beginPath();
	var path=new Path2D()
	path.moveTo(point1[0], point1[1]);
	path.lineTo(point2[0], point2[1]);
	path.lineTo(point3[0], point3[1]);
	this.bufferCanvsContext.fill(path);
	this.bufferCanvsContext.stroke();
	this.bufferCanvsContext.restore()
}

SimAnim.prototype.drawImage = function(image) {
	this.bufferCanvsContext.save()
	return new Promise(function (resolve){
		if (image.file in this.simImages)
			resolve(image)
		else {
			this.simImages[image.file] = new Image();
			this.simImages[image.file].onload = () => {
				resolve(image)
			}
			this.simImages[image.file].src = pathJoin([this.imgPath, image.file]) + '?' + new Date().getTime();
		}
		
	}.bind(this)).then((image) => {
		var xy_min = this.pointToPixel([image.xy_min[0],image.xy_min[1] + image.height])
		var width = this.scalarToPixel(image.width)
		var height = this.scalarToPixel(image.height)
		this.bufferCanvsContext.drawImage(this.simImages[image.file], xy_min[0], xy_min[1], width, height);
		this.bufferCanvsContext.restore()
	});

}

//text.position [X,Y] 
SimAnim.prototype.drawText = function(text) {
	this.bufferCanvsContext.save()
	this.bufferCanvsContext.fillStyle = text.pen_color;
	var font_size = this.scalarToPixel(text.font_size)
	this.bufferCanvsContext.font = `bold ${font_size}px Courier New`;
	var position = this.pointToPixel(text.position)
	this.bufferCanvsContext.fillText(text.content, position[0], position[1]);
	this.bufferCanvsContext.restore()
}

SimAnim.prototype.restore = function() {
	this.bufferCanvsContext.setTransform(1, 0, 0, 1, 0, 0);
}

//point[0] point around which we rotate
//point[1] angle
SimAnim.prototype.rotate = function(point) {
	var scaledPoint = this.pointToPixel(point[0])
	this.bufferCanvsContext.translate( scaledPoint[0], scaledPoint[1]);
	this.bufferCanvsContext.rotate(point[1]);
	this.bufferCanvsContext.translate(- scaledPoint[0], - scaledPoint[1]);
}

window.addEventListener('load',function() {
	// init pyodide
	languagePluginLoader.then(() =>
		pyodide.runPythonAsync(`
	import sys
	import traceback
	import io
	import js
	import micropip
	micropip.install('utils')
	micropip.install('${document.location.origin}/_static/simanim-0.0.4-py3-none-any.whl').then(js.pythonInicijalizovan())
	`)
	).then(() => {
		animations = document.getElementsByClassName('simanim')
		for (var i = 0; i < animations.length; i++) {
			simanimList[animations[i].id] = new SimAnim(animations[i])			
		}
	});

});

function pythonInicijalizovan() {
	pythonInitialized = true;
}

function queDrawEvent(event){
	if(pyodideCodeList[event.animation_key])
		pyodideCodeList[event.animation_key].queueDrawEvent(event.type, event.object)
	else{
		simanimList[event.animation_key].queueDrawEvent(event.type, event.object)
	}
}

function pathJoin(parts, sep){
	var separator = sep || '/';
	var replace   = new RegExp(separator+'{1,}', 'g');
	return parts.join(separator).replace(replace, separator);
 }
 
 function popAttribute(element, atribute, fallback){
	var atr = fallback;
	if (element.hasAttribute(atribute)){
		atr = element.getAttribute(atribute)
		element.removeAttribute(atribute)
	}
	return atr;
 }

 function throwError(msg){
	throw msg
}

window.addEventListener('resize', function(){
	for (var id in simanimList){
		simanimList[id].rescale()
		simanimList[id].stopSim()
	}
});