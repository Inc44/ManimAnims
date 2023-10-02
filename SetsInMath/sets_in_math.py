from manim import *
config.frame_height=6
config.frame_rate=60
config.frame_width=6
config.pixel_height=2**10
config.pixel_width=2**10
config.transparent=True
class SetsInMath(Scene):
	def z(self,b,c,d,e,f=None):
		if not f:
			self.play(Create(b),Write(c.next_to(b.get_top(),DOWN,buff=0.1)),Write(d,run_time=0.5),Write(e,run_time=0.5))
		else:
			self.play(Create(b.next_to(f,RIGHT,buff=0.1)),Write(c.next_to(b.get_top(),DOWN,buff=0.1)),Write(d,run_time=0.5),Write(e,run_time=0.5))
	def y(self,g,h,i,j,k,l=None):
		if l == None:
			self.z(g[k],h[k],i[k],j[k])
		else:
			self.z(g[k],h[k],i[k],j[k],g[l])
	def x(self,g,h,d,e,m=0.5):
		self.play(VGroup(*g,*h).animate.scale(m),Unwrite(d,run_time=0.5),Unwrite(e,run_time=0.5))
	def w(self,g,h,i,j,k,m=0.5):
		self.x(g[:k+1],h[:k+1],i[k],j[k],m)
	def v(self,g,h,d,e):
		self.play(ApplyMethod(VGroup(*g,*h).shift,LEFT*1.25),Unwrite(d,run_time=0.5),Unwrite(e,run_time=0.5))
	def construct(self):
		a=Text("Sets in math")
		self.play(Write(a))
		self.wait()
		self.play(Unwrite(a))
		def u(n,c,d,e):
			return[Circle(stroke_color=n,radius=1.2),MathTex(c),Text(d).shift(DOWN*2),MathTex(e).shift(UP*2)]
		o=[
			u(RED,r"\mathbb{N}","Natural",r"1,2,3"),
			u(ORANGE,r"\mathbb{W}","Whole",r"0,1,2"),
			u(YELLOW,r"\mathbb{Z}","Integer",r"-1,0,1"),
			u(GREEN,r"\mathbb{D}","Decimal",r"0.25,0.33,0.5"),
			u(TEAL,r"\mathbb{Q}","Rational",r"\frac{1}{3},\frac{1}{6},\frac{1}{7}"),
			u(BLUE,r"\mathbb{I}","Irrational",r"\sqrt{2},\sqrt{3},\phi"),
			u(PURPLE,r"\mathbb{T}","Transcendental",r"ln(2),\pi,e"),
			u(RED,r"\mathbb{A}","Algebraic",r"\sqrt{2},\frac{1}{6},\phi"),
			u(ORANGE,r"\mathbb{R}","Real",r"\sqrt{2},\pi,\phi"),
			u(YELLOW,r"\mathbb{P}","Pure Imaginary",r"2i,3i,5i"),
			u(GREEN,r"i\mathbb{R}","Imaginary",r"0,2i,3i"),
			u(TEAL,r"\mathbb{C}","Complex",r"1+2i,ln(2)+\pi i"),
			u(BLUE,r"\mathbb{H}","Quaternions",r"1+i+j+k"),
			u(PURPLE,r"\mathbb{O}","Octonions",r"e_0,\dots,e_7"),
			u(RED,r"\mathbb{S}","Sedenions",r"e_0,\dots,e_{15}"),
		]
		g=[o[p][0] for p in range(len(o))]
		h=[o[p][1] for p in range(len(o))]
		i=[o[p][2] for p in range(len(o))]
		j=[o[p][3] for p in range(len(o))]
		for k in range(0,4):
			self.y(g,h,i,j,k)
			self.wait()
			self.w(g,h,i,j,k)
		self.y(g,h,i,j,4)
		self.wait()
		self.v(g[:5],h[:5],i[4],j[4])
		self.y(g,h,i,j,5,4)
		self.wait()
		self.w(g,h,i,j,5,0.4)
		self.y(g,h,i,j,6)
		self.wait()
		self.v(g[:7],h[:7],i[6],j[6])
		self.y(g,h,i,j,7,6)
		self.wait()
		self.w(g,h,i,j,7,0.4)
		self.y(g,h,i,j,8)
		self.wait()
		self.v(g[:9],h[:9],i[8],j[8])
		self.y(g,h,i,j,9,8)
		self.wait()
		self.x(g[9],h[9],i[9],j[9])
		self.y(g,h,i,j,10,8)
		self.wait()
		self.w(g,h,i,j,10,0.4)
		for k in range(11,14):
			self.y(g,h,i,j,k)
			self.wait()
			self.w(g,h,i,j,k)
		self.y(g,h,i,j,14)
		self.wait()
		self.play(FadeOut(VGroup(*g,*h)),Unwrite(i[14],run_time=0.5),Unwrite(j[14],run_time=0.5))
		q=Text("Stay curious!").shift(UP)
		r=Text("More math")
		s=Text("wonders ahead!").shift(DOWN)
		self.play(Write(q),Write(r),Write(s))
		self.wait(3)
		self.play(Unwrite(q),Unwrite(r),Unwrite(s))