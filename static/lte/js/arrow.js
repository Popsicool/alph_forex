function changeArrow()
        {

            var current = document.getElementById('pop1').className;
            alert(current)

            if (current == 'icon-arrow-left')
            {
                // document.getElementById("MyElement").className = "MyClass";
                alert("yes")
                current = 'icon-arrow-down'
            }

            else
            {
               current.classList.replace('icon-arrow-left')
            }
        }    