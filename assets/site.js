/* AI RI Hub prototype — theme, nav, hero rotation */
(function(){
  var KEY='airi-theme', root=document.documentElement;
  try{ var saved=localStorage.getItem(KEY); if(saved) root.setAttribute('data-theme',saved); }catch(e){}

  document.addEventListener('DOMContentLoaded',function(){
    var tbtn=document.getElementById('themeToggle');
    function label(){ var d=root.getAttribute('data-theme')==='dark'; if(tbtn){tbtn.textContent = d ? 'Light mode' : 'Dark mode'; tbtn.setAttribute('aria-pressed', d?'true':'false');} }
    label();
    if(tbtn) tbtn.addEventListener('click',function(){
      var d=root.getAttribute('data-theme')==='dark';
      root.setAttribute('data-theme', d?'light':'dark');
      try{ localStorage.setItem(KEY, d?'light':'dark'); }catch(e){}
      label();
    });

    var sz=document.getElementById('textSize');
    if(sz) sz.addEventListener('change',function(){ document.body.style.fontSize=this.value; });

    var burger=document.getElementById('burger'), nav=document.getElementById('primaryNav');
    if(burger&&nav) burger.addEventListener('click',function(){
      var open=nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open?'true':'false');
    });

    /* hero slides */
    var slides=[].slice.call(document.querySelectorAll('.slide'));
    if(slides.length>1){
      var dots=[].slice.call(document.querySelectorAll('.dot')), i=0, timer=null, playing=true;
      var pause=document.getElementById('heroPause');
      var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      function show(n){
        slides.forEach(function(s,k){ s.classList.toggle('on',k===n); });
        dots.forEach(function(d,k){ d.setAttribute('aria-selected', k===n?'true':'false'); });
        i=n;
      }
      function start(){ if(reduce) return; stop(); timer=setInterval(function(){ show((i+1)%slides.length); },7000); }
      function stop(){ if(timer){clearInterval(timer); timer=null;} }
      dots.forEach(function(d,k){ d.addEventListener('click',function(){ show(k); stop(); playing=false; if(pause)pause.textContent='Play'; }); });
      if(pause){
        if(reduce){ pause.textContent='Play'; playing=false; }
        pause.addEventListener('click',function(){
          playing=!playing; if(playing){start(); pause.textContent='Pause';} else {stop(); pause.textContent='Play';}
        });
      }
      show(0); start();
    }
  });
})();
