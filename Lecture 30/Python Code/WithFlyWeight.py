import sys


# Flyweight - stores only intrinsic state
class AsteroidFlyweight:
    def __init__(self, length, width, weight, color, texture, material):
        self.length = length
        self.width = width
        self.weight = weight
        self.color = color
        self.texture = texture
        self.material = material

    def render(self, posX, posY, velocityX, velocityY):
        print(f"Rendering {self.color}, {self.texture}, {self.material} asteroid "
              f"at ({posX},{posY}) Size: {self.length}x{self.width} "
              f"Velocity: ({velocityX}, {velocityY})")

    @staticmethod
    def get_memory_usage():
        return (
            sys.getsizeof(0) * 3 +     # ints
            sys.getsizeof("") * 3 +    # strings
            32 * 3                     # approx string storage
        )


# Flyweight Factory
class AsteroidFactory:
    _flyweights = {}

    @staticmethod
    def get_asteroid(length, width, weight, color, texture, material):
        key = f"{length}_{width}_{weight}_{color}_{texture}_{material}"
        if key not in AsteroidFactory._flyweights:
            AsteroidFactory._flyweights[key] = AsteroidFlyweight(
                length, width, weight, color, texture, material
            )
        return AsteroidFactory._flyweights[key]

    @staticmethod
    def get_flyweight_count():
        return len(AsteroidFactory._flyweights)

    @staticmethod
    def get_total_flyweight_memory():
        return len(AsteroidFactory._flyweights) * AsteroidFlyweight.get_memory_usage()

    @staticmethod
    def cleanup():
        AsteroidFactory._flyweights.clear()


# Context - stores extrinsic state
class AsteroidContext:
    def __init__(self, flyweight, posX, posY, velX, velY):
        self.flyweight = flyweight
        self.posX = posX
        self.posY = posY
        self.velocityX = velX
        self.velocityY = velY

    def render(self):
        self.flyweight.render(self.posX, self.posY, self.velocityX, self.velocityY)

    @staticmethod
    def get_memory_usage():
        return sys.getsizeof(None) + sys.getsizeof(0) * 4


# Space Game with Flyweight
class SpaceGameWithFlyweight:
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
            flyweight = AsteroidFactory.get_asteroid(
                sizes[type_idx], sizes[type_idx], sizes[type_idx] * 10,
                colors[type_idx], textures[type_idx], materials[type_idx]
            )
            context = AsteroidContext(
                flyweight,
                100 + i * 50,   # posX
                200 + i * 30,   # posY
                1,              # velocityX
                2               # velocityY
            )
            self.asteroids.append(context)

        print(f"Created {len(self.asteroids)} asteroid contexts")
        print(f"Total flyweight objects: {AsteroidFactory.get_flyweight_count()}")

    def render_all(self):
        print("\n--- Rendering first 5 asteroids ---")
        for asteroid in self.asteroids[:5]:
            asteroid.render()

    def calculate_memory_usage(self):
        context_memory = len(self.asteroids) * AsteroidContext.get_memory_usage()
        flyweight_memory = AsteroidFactory.get_total_flyweight_memory()
        return context_memory + flyweight_memory

    def get_asteroid_count(self):
        return len(self.asteroids)


if __name__ == "__main__":
    ASTEROID_COUNT = 1000000

    print("\nTESTING WITH FLYWEIGHT PATTERN")
    game = SpaceGameWithFlyweight()

    game.spawn_asteroids(ASTEROID_COUNT)
    game.render_all()

    total_memory = game.calculate_memory_usage()

    print("\n=== MEMORY USAGE ===")
    print(f"Total asteroids: {ASTEROID_COUNT}")
    print(f"Memory per asteroid context: {AsteroidContext.get_memory_usage()} bytes")
    print(f"Total memory used: {total_memory} bytes")
    print(f"Memory in MB: {total_memory / (1024.0 * 1024.0):.2f} MB")
