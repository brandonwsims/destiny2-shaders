import cv2


if __name__ == '__main__':
    # Open shader
    shader = cv2.imread('./data/f1a6b54cd2e30a808a1dbfe276ee335f.jpg')
    shader = cv2.cvtColor(shader, cv2.COLOR_BGR2RGB)

    # Dimensions are 96x96
    height = width = 96

    # Compute the (almost) center point of each quadrant
    # Read as y, x with origin (0, 0) in top left corner
    # x increases horizontally as it goes right
    # y increases vertically as it goes down
    quadrants = [
        [int(height * .25), int(width * .5)],
        [int(height * .5),  int(width * .75)],
        [int(height * .75), int(width * .5)],
        [int(height * .5),  int(width * .25)]
    ]

    # When populated, will read as
    # 0 - Plating Primary
    # 1 - Plating Secondary
    # 2 - Cloth Primary
    # 3 - Cloth Secondary
    colors = []

    # Get color at each quadrant
    for i, q in enumerate(quadrants):
        # Get all pixels in a D8, including center pixel
        d8 = [
            shader[q[0],    q[1]],
            shader[q[0],    q[1]+1],
            shader[q[0],    q[1]-1],
            shader[q[0]+1,  q[1]],
            shader[q[0]+1,  q[1]+1],
            shader[q[0]+1,  q[1]-1],
            shader[q[0]-1,  q[1]],
            shader[q[0]-1,  q[1]+1],
            shader[q[0]-1,  q[1]-1]
        ]

        # For averaged rgb values
        r = g = b = 0

        # Add rgb values in D8 plus center
        for pixel in d8:
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]

        # Average rgb values for D8 plus center
        r = int(r / len(d8))
        g = int(g / len(d8))
        b = int(b / len(d8))

        # Display for testing purposes
        print('Quadrant {}, ({}, {}): rgb({}, {}, {})'.format(
            i+1, q[0], q[1], r, g, b))

        # Add to list
        colors.append((r, g, b))
