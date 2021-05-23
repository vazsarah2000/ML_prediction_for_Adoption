
    function val_func() {

    document.getElementById("tab2").disabled = true;
    var y = document.getElementById("age").value;
    var ddl = document.getElementById("income");
 	var selectedValue = ddl.options[ddl.selectedIndex].value;

    if (document.getElementById("R-married").checked == false && document.getElementById("R-single").checked == false )
    {
    alert("Relation not selected!");
    }

    else if (y==isNaN(y))
    {
        alert("Please Enter Age");
    }

    else if (document.getElementById("R-single").checked == true && (y < 45 || y > 55))
    {
    alert("Not an Eligible Age for Single Adoptive Applicant ");
    }
    else if (document.getElementById("R-married").checked == true && (y < 90 || y > 110))
    {
    alert("Not an Eligible Age for Married Adoptive Applicant ");
    }

 	else if (selectedValue == "")
    {
    alert("Please select an income range");

    }
    else
    {
    document.getElementById("tab2").disabled = false;
    }
    }

