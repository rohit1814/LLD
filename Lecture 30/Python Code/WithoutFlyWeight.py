import sys

class Asteroid:
    def __init__(self, length, width, weight, color, texture, material,
                 posX, posY, velX, velY):
        # Intrinsic properties
        self.length = length
        self.width = width
        self.weight = weight
        self.color = color
        self.texture = texture
        self.material = material

        # Extrinsic properties
        self.posX = posX
        self.posY = posY
        self.velocityX = velX
        self.velocityY = velY

    def render(self):
        print(f"Rendering {self.color}, {self.texture}, {self.material} asteroid "
              f"at ({self.posX},{self.posY}) Size: {self.length}x{self.width} "
              f"Velocity: ({self.velocityX}, {self.velocityY})")

    @staticmethod
    def get_memory_usage():
        # Rough estimation similar to C++ code
        return (
            sys.getsizeof(0) * 7 +      # ints
            sys.getsizeof("") * 3 +     # string objects
            32 * 3                      # assume ~10 char per string
        )


class SpaceGame:
    def __init__(self):
        self.asteroids = []

    def spawn_asteroids(self, count):
        print(f"\n=== Spawning {count} asteroids ===")

        colors = ["Red", "Blue", "Gray"]
        textures = ["Rocky", "Metallic", "Icy"]
        materials = ["Iron", "Stone", "Ice"]
        sizes = [25, 35, 45]

        for i in range(count):
            type_idx = i % 3
            asteroid = Asteroid(
                sizes[type_idx], sizes[type_idx], sizes[type_idx] * 10,
                colors[type_idx], textures[type_idx], materials[type_idx],
                100 + i * 50,   # x position
                200 + i * 30,   # y position
                1,              # velocityX
                2               # velocityY
            )
            self.asteroids.append(asteroid)

        print(f"Created {len(self.asteroids)} asteroid objects")

    def render_all(self):
        print("\n--- Rendering first 5 asteroids ---")
        for asteroid in self.asteroids[:5]:
            asteroid.render()

    def calculate_memory_usage(self):
        return len(self.asteroids) * Asteroid.get_memory_usage()

    def get_asteroid_count(self):
        return len(self.asteroids)


if __name__ == "__main__":
    ASTEROID_COUNT = 1000000

    print("\n TESTING WITHOUT FLYWEIGHT PATTERN")
    game = SpaceGame()

    game.spawn_asteroids(ASTEROID_COUNT)
    game.render_all()

    total_memory = game.calculate_memory_usage()

    print("\n=== MEMORY USAGE ===")
    print(f"Total asteroids: {ASTEROID_COUNT}")
    print(f"Memory per asteroid: {Asteroid.get_memory_usage()} bytes")
    print(f"Total memory used: {total_memory} bytes")
    print(f"Memory in MB: {total_memory / (1024.0 * 1024.0):.2f} MB")
