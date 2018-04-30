node('master') {
    printMessage('Running Pipeline')

    stage("Fetch Source Code") {
        git 'https://github.com/arnoldokoth/lesson5'
    }

    stage("Testing") {
        sh 'python test_functions.py'
    }

    stage("Deployment") {
        if (env.BRANCH_NAME == 'master') {
            printMessage('Deploying the master branch')
        } else {
            printMessage('No deployment configured for this branch')
        }
    }

    printMessage('Pipeline Complete')
}

def printMessage(message) {
    echo "${message}"
}
