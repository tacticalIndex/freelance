--##################################################--
--############# Developed by @choppovm #############--
--##################################################--

--[[
Creating a new particleEmitter part

I made this for a person who was asking about how this would work in like 5 minutes. 
If using this in SCP:RP, use the baseplate map, and **shift the map DOWN by like 5 studs**. Otherwise, it spawns in
the middle of the baseplate, under the ground, making it annoying to get to (someone else can fix it, use vector3 or something)

Basically no effort was put into this; it's only an example with line-by-line explanations. Don't expect anything too grand.
]]

-- step 1: create a new part
local particlePart = Instance.new("Part") -- creates a new part in the game
particlePart.Size = Vector3.new(4, 1, 4) -- part size (change later)
particlePart.Anchored = true -- keep anchored so it doesn't just instantly fall
particlePart.CanCollide = false -- i'd keep false but up to you
f(particlePart) -- parents it to the map (game.Workspace)

-- step 2: add a particle emitter to that part
local particleEmitter = Instance.new("ParticleEmitter") -- creates a new ParticleEmitter
particleEmitter.Texture = "rbxassetid://1266170131" -- replace with your desired texture id, for now its just some id i got from roblox's documentation (white rings)
particleEmitter.Rate = 10 -- number of particles emitted per second
particleEmitter.Lifetime = NumberRange.new(2, 5) -- how long particles live for (min, max)
-- Number of particles = Rate * Lifetime. Don't crash the server.
particleEmitter.Speed = NumberRange.new(5, 10) -- speed of particles (min, max)
particleEmitter.Parent = particlePart -- parents the emitter to the part

-- read https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter
-- will help a ton if expanding on this script

--[[
End of script. Related resources and documentation can be found below:
- https://create.roblox.com/docs
- https://scproleplay.com/docs
]]
