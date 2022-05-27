var activeLecture = '';
var activeActivity = '';

window.addEventListener('load', function () {
	var allLectures = document.getElementsByClassName('lecture-div');
	Array.prototype.forEach.call(allLectures, function (e) {
		e.addEventListener('click', function () {
			this.nextElementSibling.classList.toggle('d-none');
			this.children[0].classList.toggle('d-none');
			this.children[1].classList.toggle('d-none');
		});
	});

	var path = decodeURI(document.location.pathname).replace('/', '');
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
			e.preventDefault();
            var lectureDiv = document.getElementById(activeLecture);
            if (document.getElementById("activity-" + activity).parentElement.previousElementSibling != null) {
                document.getElementById("activity-" + activity).parentElement.previousElementSibling.click();
            }
            else {
                document.getElementById("lecture-" + lecture).previousElementSibling.lastElementChild.click();
            }
		});

	if (document.getElementById('nextLectureLink'))
		document.getElementById('nextLectureLink').addEventListener('click', function (e) {
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
                    document.getElementById("lecture-" + lecture).nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.click();
                }
			}
        });
        
    if (activeLecture != '') {
        if (document.getElementById("activity-" + activity).parentElement.previousElementSibling == null && document.getElementById("lecture-" + lecture).previousElementSibling == null)
            document.getElementById('prevLectureLink').classList.add('invisible');
    }
});
