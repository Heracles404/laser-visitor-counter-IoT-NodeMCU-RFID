function controlArduino(action) {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "MVC/controller/switch.py", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var response = xhr.responseText;

                    if (response.includes("Pin 2 turned ON")) {
                        document.getElementById("onButton").disabled = true;
                        document.getElementById("offButton").disabled = false;
                    } else if (response.includes("Pin 2 turned OFF")) {
                        document.getElementById("onButton").disabled = false;
                        document.getElementById("offButton").disabled = true;
                    }
                }
            };
            xhr.send("action=" + action);
        }