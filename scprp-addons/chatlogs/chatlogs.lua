--##################################################--
--############# Developed by @choppovm #############--
--##################################################--

--[[
Chat Logs: Discord Webhook Integration | Developed for ARIV

A few characters are changed to avoid discord accidentally formatting messages
(e.g. *, __, ~~, etc. are all filtered and replaced)

Chatlogs are also bundled into 8 to avoid reaching discord's rate limit too fast

Note - if you're using a proxy host, check whether or not you have a limt to the
number of functions/requests you can use. If you do have a limit, maybe change
the code up a bit to avoid reaching it too fast (e.g. mine was 125k a month)
]]

local webhookProxyURL = "PROXY URL HERE" -- see javascript code for proxy website

local usernames = {}
local messages = {}

local function sendMessage(url)
    local messageFormat = ""

    for i = 1, #usernames do
        messageFormat = messageFormat .. "**" .. usernames[i] .. ":** " .. messages[i]
        if i < #usernames then
            messageFormat = messageFormat .. "\\n"
        end
    end

    local payload = "{\"content\": \"" .. messageFormat .. "\"}"

    http(url, "post",
        { ["Content-Type"] = "application/json" },
        payload
    )

    -- Clear arrays after sending
    usernames = {}
    messages = {}
end

-- Function to sanitize chat messages
local function sanitizeMessage(msg)
    -- Escape Discord markdown characters
    msg = msg:gsub("`", "’")
    msg = msg:gsub("*", "⁂")
    msg = msg:gsub("_", "—")
    msg = msg:gsub("~", "≈")
    msg = msg:gsub("\\","/")

    -- Escape double quotes to preserve JSON structure
    msg = msg:gsub('"', '″')

    -- Prevent @everyone or @here pings
    msg = msg:gsub("@", "ª")

    return msg
end

event("chatted", function(data)
    local player = data.Value[1]
    local playertext = data.Value[2]

    table.insert(usernames, player)
    table.insert(messages, sanitizeMessage(playertext))

    if #usernames >= 8 then
        sendMessage(webhookProxyURL)
    end
end)

--[[
End of script. Related resources and documentation can be found below:
- https://create.roblox.com/docs
- https://scproleplay.com/docs
]]
