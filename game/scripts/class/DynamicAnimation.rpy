init python:   
    class DynamicAnimation(renpy.display.anim.TransitionAnimation):
        def __init__(self,images,time_forward=0.1,time_reverse=0.1,time_start=0.5,time_await=0.1,
        random_delay= 2.0 + ( renpy.python.rng.random() * 3.0 )):                  
            ## Setup default image for the animation [Image, Delay, Transition]
            self.used_images = [images[0],time_start, Dissolve(time_forward)]

            ## Append a list of animations going forward
            self.setup_forward(images[1:],time_forward,time_await)

            ## Append a list of animations going in reverse
            self.setup_reverse(list(reversed(images[:-1])),time_reverse,random_delay) 
            
            ## Call Super
            super(DynamicAnimation, self).__init__( *self.used_images )

        def setup_forward(self, images,delay,time_await):
            for p,i in enumerate(images):
                ## Image
                self.used_images.append(i) 
                if (len(images)-1)==p:
                    self.used_images.append(time_await)                    
                else:
                    self.used_images.append(delay)            
                ## Transition
                self.used_images.append(Dissolve(delay))

        def setup_reverse(self, images,delay,random_delay):
            for p,i in enumerate(images):
                ## Image
                self.used_images.append(i)
                ## Delay
                if (len(images)-1)==p:
                    self.used_images.append(random_delay)                    
                else:
                    self.used_images.append(delay)                
                ## Transition
                self.used_images.append(Dissolve(delay))
       


        