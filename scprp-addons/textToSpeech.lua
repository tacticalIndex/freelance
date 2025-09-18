--##################################################--
--############# Developed by @choppovm #############--
--##################################################--

--[[
TTS - Powered by Roblox's Text To Speech Service
When sending a chat message, it'll run the message through Roblox's TTS service, converting it to audio.

Please consider the following before use:
- ***DO NOT SAVE THE MAP AT ALL WHEN USING THIS ADDON.*** Every chat message sent creates a new part, which'll completely fill up the map's allocated storage.
- Expect lag to occur due to the parts created.
- Expect gameplay disruptions to take place due to the parts created (e.g. bullet hitting the invisible tts part, camera getting stuck in the part, etcetera).
- Roblox's TTS service uses a different filter to the current one. Terms like "Discord" get blocked by roblox's chat, but aren't blocked in TTS. If TTS does block a message, check the F9 console and look for a related message there.

It's best you don't touch anything in this script other than the settings (volume and voice id). If you know what you're doing, go ahead and do whatever (maybe you can do that "to-do" part at the end of the script that I never got round to doing...)
]]

event("chatted",function(data)
    -- Defining data that'll be used
    local playerName = data.Value(1) -- unused but kept in case changes should be made later (e.g. restrict it to specific players/teams/etc)
    local playerMessage = data.Value(2)
    local wire = Instance.new("Wire")
    local ttsHandler = Instance.new("AudioTextToSpeech")
    local audioOutput = Instance.new("AudioDeviceOutput")
    
    -- Parent instance to map (puts it under game.Workspace)
    f(wire)
    f(ttsHandler)
    f(audioOutput)
    
    -- Set up text to speech
    wire.SourceInstance = ttsHandler
    wire.TargetInstance = audioOutput
    
    -- SETTINGS: ADJUST AS NEEDED
    
    ttsHandler.Volume = 10
    ttsHandler.VoiceId = "1" -- currently "British male" (https://create.roblox.com/docs/audio/objects#text-to-speech) 
    
    -- Play TTS
    ttsHandler.Text = playerMessage
    ttsHandler:Play()
    
    -- to-do: code in a part that deletes the wire after like 10 seconds of speaking
end)

--[[
End of script. Related resources and documentation can be found below:
- https://create.roblox.com/docs
- https://scproleplay.com/docs
]]
