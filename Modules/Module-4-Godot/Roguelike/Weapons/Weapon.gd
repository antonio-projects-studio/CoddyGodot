extends Node2D
class_name Weapon, "res://Art/v1.1 dungeon crawler 16x16 pixel pack/heroes/knight/weapon_sword_1.png"

export(bool) var on_floor: bool = false

export var ranged_weapon: bool = false
export var rotation_offset: int = 0

var can_active_ability: bool = true

onready var animation_player: AnimationPlayer = get_node("AnimationPlayer")
onready var hitbox: Area2D = get_node("Node2D/Sprite/Hitbox")
onready var charge_particles: Particles2D = get_node("Node2D/Sprite/ChargeParticles")



func get_input() -> void:
	if Input.is_action_just_pressed("ui_attack") and not animation_player.is_playing():
		animation_player.play("charge")
	elif Input.is_action_just_released("ui_attack"):
		if animation_player.is_playing() and animation_player.current_animation == "charge":
			animation_player.play("attack")
		elif charge_particles.emitting:
			animation_player.play("strong_attack")
			
			
func move(mouse_direction: Vector2) -> void:
	if ranged_weapon:
		rotation_degrees = rad2deg(mouse_direction.angle()) + rotation_offset
	else:
		if not animation_player.is_playing() or animation_player.current_animation == "charge":
			rotation = mouse_direction.angle()
			hitbox.knockback_direction = mouse_direction
			if scale.y == 1 and mouse_direction.x < 0:
				scale.y = -1
			elif scale.y == -1 and mouse_direction.x > 0:
				scale.y = 1
			
			
func cancel_attack() -> void:
	animation_player.play("cancel_attack")
	
	
func is_busy() -> bool:
	if animation_player.is_playing() or charge_particles.emitting:
		return true
	return false

	
	

