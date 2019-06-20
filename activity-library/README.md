# Android library demonstrator

## Activity

This is a simple Activity that communicates via websockets with the Python backend

## Setup

- Android Studio 3.5+
- Kotlin 1.3.31
- ktor websockets client

### gradle script

- add ktor version string
- add repo maven { url 'https://kotlin.bintray.com/ktor' }
- add ktor deps for core, websockets, cio
    
    gives error "More than one file was found with OS independent path 'META-INF/ktor-http.kotlin_module'"

    - this is solved by adding the block to the android section:
        packagingOptions {
        // see https://stackoverflow.com/questions/56484281/compiler-cannot-resolve-classes-in-io-ktor-client-features-logging
        exclude 'META-INF/common.kotlin_module'
        exclude 'META-INF/*.kotlin_module'
    }
- add INTERNET permission to the Manifest
- convert the project from Application to Library
    - in build.gradle: replace apply plugin: 'com.android.application' by apply plugin: 'com.android.library'
    - comment out the line with 'appicationId ...'
    - set android.libraryVariants.all

    - In Manifest.xml remove the icon and roundIcon attributes

