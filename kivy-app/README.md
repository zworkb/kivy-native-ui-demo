# Kivy-part for native UI

## setup

- clone p4a from [zworkb customizability fork](https://github.com/kivy/python-for-android/pull/1869)
- clone buildozer from [zworkb customizability fork](https://github.com/kivy/buildozer/pull/919)
- build the activity-library

## build

### buildozer.spec
- set the correct `p4a` directory (depends on your p4a location):

    p4a.source_dir = /home/phil/p4a

- set package and app name
- add ```source.include_patterns = res/*``` since we have resources
- add `websockets` to the requirements
- register `service.py` in the services: 
    
    services = websockets:service.py

- add INTERNET permission
- android-api:18, android-minapi:23, android.sdk:28
- register the custmo activity:

    android.entrypoint = org.kivy.android.SpecialActivity

- register the `java` subdir: ```android.add_src = java```

- set the  app theme:

    android.apptheme = "@style/AppTheme"

- add the activity-library

    android.add_aars = ../activity-library/app/build/outputs/aar/nativeuidemo_0.1.2-debug.aar

- add `ktor` repository 

    android.add_gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"

- add gradle dependencies:

    - org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.31
    - androidx.appcompat:appcompat:1.0.2
    - androidx.constraintlayout:constraintlayout:1.1.3
    - io.ktor:ktor-client-core:1.2.1
    - io.ktor:ktor-client-websockets:1.2.1
    - io.ktor:ktor-client-cio:1.2.1

- package-options to avoid name clashes

    android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

### compile

in the root directory of the kivy-app:

    $ buildozer android debug