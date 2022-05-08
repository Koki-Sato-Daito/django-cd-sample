<template>
  <section class="wrapper">
    <div class="container">
        <div class="content">
            <h2 class="heading">MESSAGE</h2>
            <p>テキストテキストテキストテキストテキストテキストテキストテキスト<br>テキストテキストテキストテキストテキストテキストテキストテキスト</p>
        </div>
    </div>
</section>
</template>

<style>
.wrapper{
    width:100%;
}
.wrapper .container{
    max-width:1000px;
    margin:0px auto;
    padding:80px 0px;
}
/* content */
.wrapper .content {
    padding:50px;
    text-align:center;
}
.wrapper .content .heading{
    margin:0px 0px 40px 0px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
}
</style>

<script>
export default {
  name: 'IndexPage'
}
</script>
