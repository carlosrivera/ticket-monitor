<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
@import "~bulma/sass/utilities/initial-variables";
@import "~bulma/sass/utilities/functions";
@import url('https://fonts.googleapis.com/css?family=Asap');


$family-serif: 'Asap', sans-serif;
$family-sans-serif: 'Asap', sans-serif;

//http://www.colourlovers.com/palette/4578596/Gradient_3

// 2. Set your own initial variables
// Update blue
$blue: #183268;
$link: #4ECDC4;
$info: #00A4C3;
$success: #00CE7F;
// Add pink and its invert
$pink: #ffb3b3;
$blue-invert: #fff;
// Add a serif family
$family-serif: "Merriweather", "Georgia", serif;

// 3. Set the derived variables
// Use the new pink as the primary color
$primary: #556270;
$primary-invert: $blue-invert;

@import '~bulma/bulma'
</style>
