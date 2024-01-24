extends KinematicBody2D
class_name Character, "res://Art/v1.1 dungeon crawler 16x16 pixel pack/heroes/knight/knight_idle_anim_f0.png"


const FRICTION: float = 0.15

export (int) var hp: int = 2

export (int) var accerelation: int = 40
export (int) var max_speed: int = 100

export (bool) var flying: bool = false

onready var state_machine: Node = get_node("FiniteStateMachine")
onready var animated_sprite: AnimatedSprite = get_node("AnimatedSprite")

var mov_direction: Vector2 = Vector2.ZERO
var velocity: Vector2 = Vector2.ZERO


func _physics_process(_delta: float) -> void:
 velocity = move_and_slide(velocity)
 velocity = lerp(velocity, Vector2.ZERO, FRICTION)


func move() -> void:
 mov_direction = mov_direction.normalized()
 velocity += mov_direction * accerelation
 velocity = velocity.limit_length(max_speed)
