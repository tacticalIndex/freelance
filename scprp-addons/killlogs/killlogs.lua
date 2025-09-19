--##################################################--
--############# Developed by @choppovm #############--
--##################################################--

--[[
Kill Logs: Discord Webhook Integration | Developed for ARIV

Kill logs are bundled into 4 to avoid reaching discord's rate limit too fast

Note - if you're using a proxy host, check whether or not you have a limt to the
number of functions/requests you can use. If you do have a limit, maybe change
the code up a bit to avoid reaching it too fast (e.g. mine was 125k a month)
]]

local webhookProxyURL = "https://area-55.netlify.app/.netlify/functions/killlogsproxy" -- see javascript code for proxy website

local killers = {}
local victims = {}
local timestamps = {}

local function sendMessage(url)
    local messageFormat = ""

    for i = 1, #killers do
        messageFormat = messageFormat .. "**" .. killers[i] .. "** killed **" .. victims[i] .. "** at <t:" .. timestamps[i] .. ":T> (HH:MM:SS)."
        if i < #killers then
            messageFormat = messageFormat .. "\\n"
        end
    end

    local payload = "{\"content\": \"" .. messageFormat .. "\"}"

    http(url, "post",
        { ["Content-Type"] = "application/json" },
        payload
    )

    -- Clear arrays after sending
    killers = {}
    victims = {}
    timestamps = {}
end

event("kill", function(data)
    local playerKiller = data.Value[1]
    local playerVictim = data.Value[2]
    local timeOfKill = os.time()

    table.insert(killers, playerKiller)
    table.insert(victims, playerVictim)
    table.insert(timestamps, timeOfKill)

    if #killers >= 5 then
        sendMessage(webhookProxyURL)
    end
end)

--[[
End of script. Related resources and documentation can be found below:
- https://create.roblox.com/docs
- https://scproleplay.com/docs
]]
