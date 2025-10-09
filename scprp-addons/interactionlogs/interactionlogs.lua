--##################################################--
--############# Developed by @choppovm #############--
--##################################################--

--[[
Interaction Logs: Discord Webhook Integration | Developed for ARIV

Note - this is only for CUSTOM INTERACTIONS. Regular ones (e.g. doors) will not work; only
the custom interactions made with F3X (from that one props preset, idk which one) will.

I get this is kind of useless, but my original idea for keeping it was to make it so that when
you interacted with a part in-game, you could start/end a staff member's shift, with this 
addon interacting with the ariv website (see my GitHub, now deprecated but code is available).

Maybe someone can implement this themselves...? *wink wink nudge nudge*
]]

-- Proxy URL that forwards data to Discord
local webhookProxyURL = "PROXY URL HERE" -- see javascript code for proxy website

-- Event listener for custom interactions
event("interaction", function(data)
    local player = data.Value[1]
    local usedinteraction = data.Value[2]

    local messageFormat = "**" .. player .. "** interacted with " .. usedinteraction

    http(webhookProxyURL, "post",
        { ["Content-Type"] = "application/json" },
        "{\"content\": \"" .. messageFormat .. "\"}"
    )
end)

event("lightswitch", function(data)
    local player = data.Value[1]
    local room = data.Value[2]
    local state = data.Value[3]

    local messageFormat = "**" .. player .. "** turned " .. room .. "'s lights " .. state .. "."

    http(webhookProxyURL, "post",
        { ["Content-Type"] = "application/json" },
        "{\"content\": \"" .. messageFormat .. "\"}"
    )
end)

--[[
End of script. Related resources and documentation can be found below:
- https://create.roblox.com/docs
- https://scproleplay.com/docs
]]
