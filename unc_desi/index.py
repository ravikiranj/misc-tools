#!/usr/bin/python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

preHTML = '''
<!DOCTYPE HTML>
<html>
<head>
  <title>scenic_photo</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="assets/js/modernizr-1.5.min.js"></script>
</head>

<body>
  <div id="main">
    <header>
          <h2>UNC Desi Guide</h2>
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
                    <li style="padding-bottom: 0px;"><a href="#">Campus Life</a>
                        <ul style="margin: 0px;">
                            <li id="food"><a href="food.html">Food</a></li>
                            <li id="shopping"><a href="shopping.html">Shopping</a></li>
                            <li id="entertainment"><a href="entertainment.html">Sports & Entertainment</a></li>
                        </ul>
                    </li>
                    <li style="padding-bottom: 0px;"><a href="#">Academics</a>
                        <ul style="margin: 0px;">
                            <li id="books"><a href="books.html">Books</a></li>
                            <li id="courses"><a href="courses.html">Courses</a></li>
                        </ul>
                   </li>
                    <li style="padding-bottom: 0px;"><a href="#">Finance</a>
                        <ul style="margin: 0px;">
                            <li id="tuition"><a href="tuition.html">Tuition Fees Payment</a></li>
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
        html = preHTML % (('Intro', ''))
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
        addJS = script % (('post-arrival'))
        html = preHTML % (('Post-Arrival', addJS))
        self.response.out.write(html)
        
class Housing(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('housing'))
        html = preHTML % (('Housing', addJS))
        self.response.out.write(html)

class Food(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('food'))
        html = preHTML % (('Food', addJS))
        self.response.out.write(html)

class Shopping(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('shopping'))
        html = preHTML % (('Shopping', addJS))
        self.response.out.write(html)

class Entertainment(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('entertainment'))
        html = preHTML % (('Entertainment', addJS))
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

class Tuition(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('tuition'))
        html = preHTML % (('Tuition', addJS))
        self.response.out.write(html)

class Lifestyle(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        addJS = script % (('lifestyle'))
        html = preHTML % (('Lifestyle', addJS))
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
                                      ('/food.html', Food),
                                      ('/shopping.html', Shopping),
                                      ('/entertainment.html', Entertainment),
                                      ('/books.html', Books),
                                      ('/courses.html', Courses),
                                      ('/tuition.html', Tuition),
                                      ('/lifestyle.html', Lifestyle),
                                      ('/faq.html', FAQ),
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
