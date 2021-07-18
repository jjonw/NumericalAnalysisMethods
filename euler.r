solveEuler <- function(f, y0, a, b, t) {
    if(t < 1){
      h = t
      N = round((b-a)/h)
    } else if(t > 1 || t == 1) {
      h = (b-a)/float(t)
      N = t
    }
    
    vx = rep(0, N+1)
    vy = rep(0, N+1)
    vx[0] = a
    vy[0] = y0
    
    for(i in 1:N+1){
      vx[i] = a + i*h
      vy[i] = vy[i-1] + h*f(vx[i-1], vy[i-1])
    }
    
    return(vx, vy)
}
