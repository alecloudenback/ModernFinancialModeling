using Luxor

@svg begin
    # Set the background to transparent
    background(0, 0, 0, 0)
    fontface("Georgia")
    sethue("black")
    setline(0.25)

    total = 30

    radius = 55
    sethue("grey90")

    # This loop draws 28 polygons, from 3 sides to 30 sides.
    for i in 3:total
        global radius # Required because the loop modifies 'radius' from the outer scope


        # Create a regular polygon with 'i' sides
        p = ngon(outerframe[1], radius, i, 0, vertices = true)

        # Stroke the polygon's path and add a red dot at the center
        prettypoly(p, action = :stroke, close = true, () -> (sethue("grey90"); circle(O, 2, action = :fill)))

        # Calculate geometric properties
        pa = polyarea(p)
        pp = polyperimeter(p)
        ppoverradius = pp / radius

        # Increase the radius for the next polygon to create the spiral effect
        radius += 5
    end


end 800 800 "draw.svg"
