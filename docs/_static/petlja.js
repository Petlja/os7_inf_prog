var activeLecture = '';
var activeActivity = '';

window.addEventListener('load', function () {
	var allLectures = document.getElementsByClassName('lecture-div');
	Array.prototype.forEach.call(allLectures, function (e) {
		e.addEventListener('click', function () {
			this.nextElementSibling.classList.toggle('d-none');
			this.children[1].classList.toggle('d-none');
			this.children[2].classList.toggle('d-none');
		});
	});
    var allLectures = document.getElementsByClassName('studioLecture');
	Array.prototype.forEach.call(allLectures, function (e) {
		e.addEventListener('click', function () {
            localStorage.setItem('scrollpos',0);
		});
	});
	var path = decodeURI(document.location.pathname).split('/').slice(-2).join('/');
	path = path.replaceAll(' ', '%20');
	var lecture = path.substring(0, path.indexOf('/'));
	var activity = path.substring(path.indexOf('/') + 1).replace('.html', '');

	if (document.getElementById("lecture-" + lecture)) {
		document.getElementById("lecture-" + lecture).click();
		activeLecture = lecture;
	}

	if (document.getElementById("activity-" + activity)) {
		document.getElementById("activity-" + activity).classList.add('active');
		activeActivity = activity;
	}

	if (document.getElementById('prevLectureLink'))
		document.getElementById('prevLectureLink').addEventListener('click', function (e) {
            localStorage.setItem('scrollpos',0);
			e.preventDefault();
            var lectureDiv = document.getElementById(activeLecture);
            if (document.getElementById("activity-" + activity).parentElement.previousElementSibling != null) {
                document.getElementById("activity-" + activity).parentElement.previousElementSibling.click();
            }
            else {
                document.getElementById("activity-" + activity).parentElement.parentElement.parentElement.previousElementSibling.children[1].lastElementChild.click()
            }
		});

	if (document.getElementById('nextLectureLink'))
		document.getElementById('nextLectureLink').addEventListener('click', function (e) {
            localStorage.setItem('scrollpos',0);
			e.preventDefault();
			if (activeLecture == '') {
				var lectureDiv = document.getElementsByClassName('lecture-div')[0];
				lectureDiv.nextElementSibling.firstElementChild.click();
			} else {
                var lectureDiv = document.getElementById(activeLecture);
                if (document.getElementById("activity-" + activity).parentElement.nextElementSibling != null) {
                    document.getElementById("activity-" + activity).parentElement.nextElementSibling.click();
                }
                else {
					document.getElementById("lecture-" + lecture).parentElement.nextElementSibling.children[1].firstChild.click()
                }
			}
        });
        
    if (activeLecture != '') {
        if (document.getElementById("activity-" + activity).parentElement.parentElement.parentElement.previousElementSibling == null && document.getElementById("activity-" + activity).parentElement.previousElementSibling == null)
            document.getElementById('prevLectureLink').classList.add('invisible');
    }

	if (document.getElementsByClassName('course-requirements').length > 0) {
		var learningDiv = document.getElementsByClassName("course-requirements")[0].firstElementChild;
		var learningDivList = learningDiv.querySelector('ul');
		var numberOfLiElements = learningDivList.querySelectorAll('li').length;


		var btnSeeMore = document.getElementById('seeMoreReqs')
		var btnSeeLess = document.getElementById('seeLessReqs')

		btnSeeMore.addEventListener('click', function () {
			learningDivList.setAttribute('style', 'max-height: none !important; overflow: auto;');
			document.getElementById('seeMoreReqs').style.display = 'none';
			document.getElementById('seeLessReqs').style.display = 'block';
		})

		btnSeeLess.addEventListener('click', function () {
			learningDivList.setAttribute('style', '');
			document.getElementById('seeMoreReqs').style.display = 'block';
			document.getElementById('seeLessReqs').style.display = 'none';
		})

	}
	if(document.getElementById("content-header-label")){
		document.getElementById("content-header-label").addEventListener("click",function(){
			window.location.href = "../"
		})
	}
    if (document.getElementById('decLetterIcon')){
        document.getElementById('decLetterIcon').addEventListener('click', function () {
            decrAllFontSize();
        });
	}
    if (document.getElementById('fontSizeToggle')) {
        document.getElementById('fontSizeToggle').addEventListener('click', function () {
            document.getElementById('fontChangeModal').classList.toggle('d-none');
        });
    }

    if (document.getElementById('incLetterIcon')){
        document.getElementById('incLetterIcon').addEventListener('click', function () {
            incrAllFontSize();
        });
	}
    var main = document.getElementsByClassName('lectureContentMaterial')[0]
    var scrollpos = localStorage.getItem('scrollpos');
    if (main && scrollpos){
        main.scrollTop = scrollpos;

        document.getElementsByClassName('lectureContentMaterial')[0].addEventListener('scroll', function(e) {
            var main = document.getElementsByClassName('lectureContentMaterial')[0]
            localStorage.setItem('scrollpos', main.scrollTop);
        });
    }
});

function incrAllFontSize() {
    $("*").each(function (index, elem) {
        var $this = $(this);//caching for perf. opt.

        var curr = $this.css("fontSize");//get the fontSize string
        if (curr != "" && curr != undefined) {//check if it exist
            curr = curr.replace(/px$/, "");//get rid of "px" in the string

            var float_curr = parseFloat(curr);//convert string to float

            if(float_curr < 49)
                float_curr += 1;//actual incr

            var new_val = "" + float_curr + "px";//back to string
            $this.css("fontSize", new_val);//set the fontSize string
        }
    });


    document.getElementById('currentFontSize').innerHTML = parseInt(document.getElementById('currentFontSize').innerHTML) + 1;
}


function decrAllFontSize() {
    $("*").each(function (index, elem) {
        var $this = $(this);//caching for perf. opt.

        var curr = $this.css("fontSize");//get the fontSize string
        if (curr != "" && curr != undefined) {//check if it exist
            curr = curr.replace(/px$/, "");//get rid of "px" in the string

            var float_curr = parseFloat(curr);//convert string to float
            if (float_curr > 6)
                float_curr -= 1;//actual incr

            var new_val = "" + float_curr + "px";//back to string
            $this.css("fontSize", new_val);//set the fontSize string
        }
    });

    document.getElementById('currentFontSize').innerHTML = parseInt(document.getElementById('currentFontSize').innerHTML) - 1;
}