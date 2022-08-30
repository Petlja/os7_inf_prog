$(document).ready(function () {
    $("[data-level]").each(function (index) { 
        var level=$(this).attr('data-level');
        $(this).parent(".section").addClass('rst-level rst-level-'+level);
    });
    if (document.querySelector('.learnmorenote-type .course-content p:nth-of-type(1)')) {
        var allNodes = document.querySelectorAll('.learnmorenote-type .course-content p:nth-of-type(1)');
        for (var i = 0; i < allNodes.length; i++) {
            allNodes[i].addEventListener('click', function (e) {
                var parent = e.currentTarget.parentNode;
                var allParas = parent.querySelectorAll('.learnmorenote-type .course-content p:not(:nth-of-type(1))');
                e.currentTarget.classList.toggle('expanded');
                for (var j = 0; j < allParas.length; j++) {
                    if (allParas[j].style.display != 'block') 
                        allParas[j].style.display = 'block';
                    else
                        allParas[j].style.display = 'none';
                }
            });
        }
    }
});