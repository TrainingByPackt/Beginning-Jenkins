node {
   stage("Might Run On Node 1 Or Master") {
       printMessage("Running")
       sh 'sleep 10'
       sh 'hostname'
   }
}

node('node2') {
    stage("On Node 2") {
        printMessage("Running On Node 2")
        sh 'sleep 10'
        sh 'hostname'
    }
}

def printMessage(message) {
    echo "${message}"
}
