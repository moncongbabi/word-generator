/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/

job("Build and run tests") {
    startOn {
        gitPush { enabled = true }
        schedule { cron("0 */1 * * *") } 
    }
    parallel {
		
        
           container(displayName = "test", image = "ubuntu") {
             	resources {
                    cpu = 4.cpu
                    memory = 4000.mb
                }

                shellScript {
                    content = """
                    	apt update -y && apt install -y python3 python3-pip curl wget
                        pip install -r requirements.txt && python3 app.py
                    """
                }
            }
      }
}

