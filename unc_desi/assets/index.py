#!/usr/bin/python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

preHTML = '''
<!DOCTYPE HTML>
<html>
<head>
  <title>UNC New International Grad Student Unofficial Guide</title>
  <meta name="description" content="UNC New International Grad Student Unofficial Guide. This is mostly targeted at South Asian Students coming from India, Pakistan, Bangladesh, Afghanistan, Bhutan, Maldives, Nepal and Srilanka" />
  <meta name="keywords" content="indian graduate student association unc, help indian grad student unc, unc indian, unc indian student" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="assets/js/modernizr-1.5.min.js"></script>
</head>

<body>
  <div id="main">
    <header>
        <h2>UNC New International Grad Student Unofficial Guide</h2>
    </header>
    <div id="site_content">
      <div id="sidebar_container">
        <div class="sidebar">
            <nav>
                <ul id="main-nav">
                    <li id="intro" class="active"><a href="/">Introduction</a></li>
                    <li id="packing"><a href="packing.html">Packing</a></li>
                    <li id="pre-arrival"><a href="pre-arrival.html">Pre-Arrival</a></li>
                    <li id="airport-pickup"><a href="airport-pickup.html">Airport Pickup</a></li>
                    <li id="post-arrival"><a href="post-arrival.html">Post-Arrival</a></li>
                    <li id="housing"><a href="housing.html">Housing</a></li>
                    <li id="campus-life" style="padding-bottom: 0px;"><a href="campus-life.html">Campus Life</a>
                        <ul style="margin: 0px;">
                            <li id="food" style="margin-top: 5px;"><a href="food.html">Food</a></li>
                            <li id="shopping"><a href="shopping.html">Shopping</a></li>
                            <li id="sports"><a href="sports.html">Sports</a></li>
                            <li id="transportation"><a href="transportation.html">Transportation</a></li>
                            <li id="music"><a href="music.html">Music</a></li>
                        </ul>
                    </li>
                    <li id="academics" style="padding-bottom: 0px;"><a href="academics.html">Academics</a>
                        <ul style="margin: 0px;">
                            <li id="books" style="margin-top: 5px;"><a href="books.html">Books</a></li>
                            <li id="courses"><a href="courses.html">Courses</a></li>
                        </ul>
                   </li>
                    <li id="finance" style="padding-bottom: 0px;"><a href="finance.html">Finance</a>
                        <ul style="margin: 0px;">
                            <li id="tuition" style="margin-top: 5px;"><a href="tuition.html">Tuition Fees Payment</a></li>
                            <li id="lifestyle"><a href="lifestyle.html">Lifestyle</a></li>
                        </ul>
                    </li>
                    <li id="faq"><a href="faq.html">FAQ</a></li>
                </ul>
            </nav>
        </div>
      </div>
      </hr>
      <div class="content">
      %s <!-- Content --> 
      </div>
    </div>
    <footer>
    </footer>
  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="assets/js/jquery-1.8.0.min.js"></script>
  %s <!-- JS -->
</body>
</html>
'''
#script
script = '''
<script type="text/javascript">
function init(){
    var prevId = document.getElementsByClassName('active')[0];
    prevId.className = '';
    var currId = document.getElementById("%s");
    currId.className = 'active';
}
window.onload = init;
</script>
'''

class Intro(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/intro.html', 'r').read()
        html = preHTML % ((markup, ''))
        self.response.out.write(html)

class Packing(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('packing'))
        html = preHTML % (('Packing', addJS))
        self.response.out.write(html)

class PreArrival(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('pre-arrival'))
        html = preHTML % (('Pre-Arrival', addJS))
        self.response.out.write(html)

class AirportPickup(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('airport-pickup'))
        html = preHTML % (('Airport Pickup', addJS))
        self.response.out.write(html)

class PostArrival(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/post-arrival.html', 'r').read()
        addJS = script % (('post-arrival'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Housing(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('housing'))
        html = preHTML % (('Housing', addJS))
        self.response.out.write(html)

class CampusLife(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/campus-life.html', 'r').read()
        addJS = script % (('campus-life'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Food(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/food.html', 'r').read()
        addJS = script % (('food'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Shopping(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/shopping.html', 'r').read()
        addJS = script % (('shopping'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Sports(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/sports.html', 'r').read()
        addJS = script % (('sports'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Transportation(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/transportation.html', 'r').read()
        addJS = script % (('transportation'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class Music(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/music.html', 'r').read()
        addJS = script % (('music'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)
        
class Academics(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('academics'))
        html = preHTML % (('Academics', addJS))
        self.response.out.write(html)

class Books(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('books'))
        html = preHTML % (('Books', addJS))
        self.response.out.write(html)

class Courses(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('courses'))
        html = preHTML % (('Courses', addJS))
        self.response.out.write(html)

class Finance(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('finance'))
        html = preHTML % (('Finance', addJS))
        self.response.out.write(html)

class Tuition(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('tuition'))
        html = preHTML % (('Tuition', addJS))
        self.response.out.write(html)

class Lifestyle(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        markup = ''
        markup = open('../assets/data/lifestyle.html', 'r').read()
        addJS = script % (('lifestyle'))
        html = preHTML % ((markup, addJS))
        self.response.out.write(html)

class FAQ(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('faq'))
        html = preHTML % (('FAQ', addJS))
        self.response.out.write(html)
    
application = webapp.WSGIApplication([('/', Intro),
                                      ('/packing.html', Packing),
                                      ('/pre-arrival.html', PreArrival),
                                      ('/airport-pickup.html', AirportPickup),
                                      ('/post-arrival.html', PostArrival),
                                      ('/housing.html', Housing),
                                      ('/campus-life.html', CampusLife),
                                      ('/food.html', Food),
                                      ('/shopping.html', Shopping),
                                      ('/sports.html', Sports),
                                      ('/transportation.html', Transportation),
                                      ('/music.html', Music),
                                      ('/academics.html', Academics),
                                      ('/books.html', Books),
                                      ('/courses.html', Courses),
                                      ('/finance.html', Finance),
                                      ('/tuition.html', Tuition),
                                      ('/lifestyle.html', Lifestyle),
                                      ('/faq.html', FAQ),
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
