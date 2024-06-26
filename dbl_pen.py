from manim import *
import math
def atangle(start,l,angle):
    x=start[0]
    y=start[1]
    x1=x+l*math.sin(angle)
    y1=y-l*math.cos(angle)
    return Line(start,[x1,y1,0])
class S1(Scene):
    def construct(self):
        theta1=math.pi/2
        theta2=math.pi-math.pi/6
        omega1=0
        omega2=0
        poi=[0,2,0]
        l1=2
        l2=2
        dt=0.025
        g=9.8
        d1=1
        d2=1
        m1=2
        m2=2
        head=Tex("Double Pendulum Simulation").to_edge(UP).set_fill(YELLOW_B)
        outro = Tex("Don't you love chaos?").to_edge(DOWN).set_fill(YELLOW_C)
        def alpha1(thet1,thet2,omeg1,omeg2):
            return ((m2*l2*(omeg2**2)*(math.sin(thet2-thet1)))-((m1+m2)*g*math.sin(thet1))+(m2*(math.cos(thet2-thet1))*((l1*(omeg1**2)*(math.sin(thet2-thet1)))+(g*math.sin(thet2)))))/(((m1+m2)*l1)-(m2*l1*((math.cos(thet2-thet1))**2)))
        def alpha2(thet1,thet2,omeg1,omeg2):
            a1=((m2*l2*(omeg2**2)*(math.sin(thet2-thet1)))-((m1+m2)*g*math.sin(thet1))+(m2*(math.cos(thet2-thet1))*((l1*(omeg1**2)*(math.sin(thet2-thet1)))+(g*math.sin(thet2)))))/(((m1+m2)*l1)-(m2*l1*((math.cos(thet2-thet1))**2)))
            return (-1)*(((l1*a1*(math.cos(thet2-thet1)))+(l1*(omeg1**2)*(math.sin(thet2-thet1)))+(g*(math.sin(thet2))))/(l2))

        rod1=always_redraw(lambda: atangle(poi,l1,theta1).set_stroke(width=1,color=YELLOW_A,opacity=1))
        rod2=always_redraw(lambda: atangle(rod1.get_end(),l2,theta2).set_stroke(width=1,color=YELLOW_A,opacity=1))
        bob1=always_redraw(lambda: Dot(rod1.get_end(),m1*(0.1)).set_fill([GREEN,PINK,WHITE]))
        bob2=always_redraw(lambda: Dot(rod2.get_end(),m2*(0.1)).set_fill([GREEN,PINK,WHITE]))
        pat=TracedPath(bob2.get_center,stroke_color=RED, dissipating_time=2, stroke_opacity=[0.6, 1])
        hing=Dot(poi,0.2).set_fill([GRAY_E,GRAY_A])
        self.play(DrawBorderThenFill(head),run_time=2.5)
        self.play(Create(VGroup(hing,rod1,rod2,bob1,bob2)))
        self.add(pat)
        for i in range(0,500):
            t1=theta1
            t2=theta2
            o1=omega1
            o2=omega2
            alph1=alpha1(t1,t2,o1,o2)
            alph2=alpha2(t1,t2,o1,o2)
            theta1=theta1+(dt*o1)+((((dt)**2)*alph1)/2)
            theta2=theta2+(dt*o2)+((((dt)**2)*alph2)/2)

            ko21=alpha2(t1,t2,o1,o2)
            ko22=alpha2(t1+(o1*dt/2),t2+(o2*dt/2),o1+(alph1*dt/2),o2+(ko21*dt/2))
            ko23=alpha2(t1+(o1*dt/2),t2+(o2*dt/2),o1+(alph1*dt/2),o2+(ko22*dt/2))
            ko24=alpha2(t1+(o1*dt),t2+(o2*dt),o1+(alph1*dt),o2+(ko23*dt))
            omega2=omega2+(dt*(ko21+2*ko22+2*ko23+ko24)/6)
            ko11=alpha1(t1,t2,o1,o2)
            ko12=alpha1(t1+(o1*dt/2),t2+(o2*dt/2),o1+(ko11*dt/2),o2+(alph2*dt/2))
            ko13=alpha1(t1+(o1*dt/2),t2+(o2*dt/2),o1+(ko12*dt/2),o2+(alph2*dt/2))
            ko14=alpha1(t1+(o1*dt),t2+(o2*dt),o1+(ko13*dt),o2+(alph2*dt))
            omega1=omega1+(dt*(ko11+(2*ko12)+(2*ko13)+ko14)/6)
            

            self.wait(dt)
            
        self.play(DrawBorderThenFill(outro),run_time=2.5)


            
            
            
            
