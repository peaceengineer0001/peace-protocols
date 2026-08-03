# From Windows Tenant to Digital Sovereign

*A first-person account of one migration — and an invitation to make your own.*

---

## Part One — The Story

### The slow realization

I didn't leave Windows in a fit of anger. It was quieter than that. It was a hundred small moments that added up until I couldn't un-see the shape of them.

It was the morning my ASUS ZenBook rebooted itself during a call because an update had decided its schedule outranked mine. It was the Start menu suggesting apps I never asked for, the "recommended" web results stapled to my own file searches, the account nag screen that stood between me and my own desktop. It was realizing that OneDrive had quietly become the *real* home of my documents, and that "my" files were sitting on a server whose terms of service I'd never actually read.

None of it was catastrophic. That's exactly what made it insidious. Each individual imposition was small enough to shrug off. But somewhere in there I understood that I had stopped being the owner of my computer and had become its **tenant** — permitted to live there, on someone else's terms, paying rent in attention and data, subject to eviction from features I'd come to depend on whenever the landlord changed the lease.

The machine I'd bought with my own money was working, subtly and constantly, in someone else's interest. And the better it got at "helping" me, the more of me it harvested to do so.

I'm an engineer. I don't like problems I can't inspect. And this was a problem I couldn't inspect — because the whole point of the modern consumer OS is that you're not supposed to look under the hood. You're supposed to trust. I found, one grey afternoon, that I no longer did.

### What I actually wanted

Before I knew where I was going, I knew what I was looking for. I wrote it down, because I've learned that vague longings make bad compasses.

I wanted a computer that **kept my secrets.** Whose defaults protected me instead of exposing me. Whose behavior I could read, all the way down, in plain language, and change if I disagreed with it.

But I wanted something larger than a private laptop. I'd been thinking for a long time about what it means to live sovereignly — not as a slogan, but across the real dimensions of a life. My **spiritual** center: my attention, my sense of meaning, the quiet I need to think. My **mental** life: what I learn, what I remember, who gets to shape my beliefs. My **physical** foundation: energy, water, food, shelter, health. My **economic** standing: whether I'm building wealth or just servicing subscriptions. My **community**: the people I'm actually accountable to, versus the platforms that pretend to connect us while mining the connection.

Big Tech had an answer for every one of those dimensions, and every answer was the same: *give it to us, and we'll manage it for you.* Give us your attention and we'll fill it. Give us your data and we'll organize it. Give us your money, monthly, forever, and we'll rent you back the fruits of your own life.

I wanted the opposite. I wanted tools that made me **more** capable of governing my own dimensions, not less. I wanted an AI that worked *for* me — sitting on my side of the table, reading nothing back to a corporation, answering only to me. I didn't want to be managed. I wanted to be equipped.

### Discovering NixOS

The foundation came first, and it came from an unlikely place: a Linux distribution with a reputation for being difficult.

I'd used Linux before — Ubuntu, Fedora, the usual. They were freer than Windows, certainly. But they carried the same old curse of every operating system I'd ever touched: **entropy.** Install enough software, tweak enough settings, and eventually you have a machine held together by forgotten decisions, impossible to reproduce and terrifying to upgrade. A house of cards that happened to be open source.

**NixOS** broke the curse, and it did so with one radical idea: *the entire system is described in a single configuration file.* Not "mostly." Not "the important parts." Everything. What's installed, what services run, how the network is set up, who the users are — all of it, declared in plain text, in one place.

The first time it clicked, I actually laughed out loud. My computer was no longer a *thing that happened to me over time.* It was a **document.** I could read it. I could back it up. I could put it in version control and see, line by line, every decision that made my machine what it was. And if I changed the document and ran one command, the machine became exactly what the document said — no residue, no forgotten cruft, no mystery.

Better still: every change created a new "generation," and I could roll back to any previous one from the boot menu. For the first time in my computing life, I had an operating system that **could not strand me.** An update that misbehaved wasn't a crisis; it was a reboot and a menu selection. NixOS was reproducible, inspectable, and effectively unbreakable. It was the sovereign body I'd been looking for.

But a body needs a mind.

### Building Peace Protocols

NixOS gave me a machine I could trust. It didn't, by itself, help me *govern the dimensions of my life.* That's the piece I had to build — and building it became **Peace Protocols.**

The idea was simple to say and hard to do: an AI agent for each dimension of sovereign living, all coordinated by one orchestrator, all running on hardware I controlled, none of it phoning home unless I explicitly told it to.

So I designed a **constellation of twenty agents.** Twelve of them — I call them the Resource Realms — each watch over one concrete pillar of self-sufficiency: **Sol** for energy, **Tide** for water, **Root** for food, **Heal** for health, **Haven** for shelter, **Cycle** for waste, **Lore** for knowledge, **Mesh** for communication, **Passage** for transport, **Forge** for what I make, **Thrive** for my economics, and **Council** for governance. Seven more — the Sovereign Bodies — hold the higher-order work of wellbeing and coherence. And at the center sits **Raven**, the orchestrator, who doesn't do the domain work directly but *coordinates the whole council*, runs the weekly synthesis, and computes the two metrics I care about most: the **Peace Efficiency Index** and the **Community Vitality Index** — honest numbers that tell me whether I'm actually becoming more sovereign or just telling myself I am.

Underneath the agents I built a **Unified MCP Bus** — a single nervous system that routes intelligence across 23 integrated tools, with **local inference as the primary backend** so my thinking stays on my own silicon. And because no one should be an island by decree, I made Peace Protocols an **overlay on Buzz**, an agentic harness built on the Nostr protocol, where my identity is a cryptographic key I own outright and federation with other sovereign nodes is a choice I make deliberately — never a default imposed on me.

The whole thing was designed to be **honest about what it is.** It's not magic. Every agent, every integration, every number traces back to readable code I can inspect. That was the whole point.

### The migration

Which brings me back to the ZenBook.

I could have built all of this on a server in a closet. But I wanted to prove the thing that matters most to the people I now help: that you can take an **ordinary, everyday laptop** — the exact machine millions of people already own — and turn it into a sovereign one. Not exotic hardware. Not a fortune in gear. The ThinkPad's prettier cousin, the ubiquitous ASUS ZenBook, running the same Windows 11 everyone else runs.

So I backed everything up — documents, bookmarks, the passwords I migrated into a manager I actually control — and I did the thing that still makes newcomers hold their breath: I wiped Windows off the disk.

I won't pretend there wasn't a moment. The installer showed me its summary screen, the plain-language description of exactly what it was about to do, and I sat with the finality of it for a few seconds. This was the last instant Windows existed on that machine. Then I clicked through, and the feeling that followed wasn't loss. It was **space.** The particular lightness of setting down something heavy you'd been carrying so long you'd forgotten it was heavy.

Twenty-five minutes later the ZenBook rebooted into NixOS. I logged in. I opened a terminal and looked at `/etc/nixos/configuration.nix` — my whole machine, right there, in text I could read. Then I cloned Peace Protocols, ran the flake, and rebuilt the system into PeaceOS.

### The moment it clicked

I ran the MCP Bus and watched the connection pool come up.

There's a specific kind of quiet satisfaction in watching a system you designed actually *breathe.* The bus started its servers concurrently, health-checking each one, isolating the ones whose upstream services I hadn't provisioned yet, keeping everything else alive around the gaps. The registry validated: twenty-three servers, zero errors.

Then I brought Raven online, and the council with it. Sol reporting on energy. Tide on water. Lore standing ready with the knowledge realm. And Raven at the center, coordinating, computing the indexes, holding the whole constellation in view.

I sat back in a chair in a quiet room and looked at a laptop — the *same* laptop that used to reboot itself mid-call — now running an entire sovereign intelligence layer that answered to exactly one person. Me. Nothing was being harvested. Nothing was phoning home. Nothing was working against me in the background. For the first time, every process on that machine existed because I had chosen it, and I could point to the line of text that proved it.

That was the moment it clicked. Not "I switched operating systems." Something deeper: *I stopped renting my own mind.*

### What life looks like now

The subscriptions are mostly gone, and the ones that remain are choices, not chains. My files live where I put them. My AI works on my side of the table. When I want to know what my computer is doing, I read the file that says so. When an update lands badly, I roll back and get on with my day.

But the real change isn't technical. It's a posture. I no longer relate to my tools as a supplicant hoping the landlord won't raise the rent. I relate to them as an owner — someone who understands his own house, keeps his own keys, and decides for himself which doors to open to the wider world.

I became a **digital sovereign.** And once I'd made the crossing, I couldn't stop thinking about how many people are standing exactly where I stood on that grey afternoon — feeling the hundred small impositions add up, sensing there must be another way, not knowing that the way is real and walkable and closer than they think.

So I started helping people make the crossing. That's the work now.

---

## Part Two — The Offer

### What Peace Engineers does

I run a small consulting practice, **Peace Engineers**, and the work is simple to describe: **I help people migrate from Windows and macOS to NixOS / PeaceOS, with Peace Protocols configured for their life.** End to end. From the laptop they already own to a sovereign machine they fully control.

This is the exact journey I made on that ZenBook, done *with* you and *for* you, so you don't have to become a NixOS expert to reap what NixOS offers. You bring the willingness. I bring the map, the hands, and the years of having already made every mistake so you don't have to.

### What you actually get

**A hardware assessment.** Not every machine is equally ready for this journey, and I'll tell you the truth about yours before we start. We look at your laptop or desktop, confirm what Linux needs — Wi-Fi, graphics, the fiddly bits — and plan around anything unusual. If your hardware isn't a good fit, I'll say so plainly rather than sell you a struggle.

**A custom configuration.** Your PeaceOS is not a generic image. We build your `configuration.nix` and your Peace Protocols flake around *your* actual needs — the software you rely on, the workflows you can't live without, the dimensions of sovereignty that matter most to you right now. Because it's all declared as code, your entire setup becomes a document you own and can restore or clone forever.

**Peace Protocols, installed and tuned.** We stand up the Unified MCP Bus, bring Raven and the council online, and configure the realms you want to start with. We set your privacy tiers so you know exactly what stays on your machine — which, by default, is everything. We generate and help you safeguard your Nostr identity keys. You leave with a working constellation, not a pile of parts.

**Thirty days of onboarding support.** The migration is a day. The *habit* of sovereignty is a season. For a full month afterward I'm available to answer the questions that only surface once you're living in the new house — the "how do I…" and the "why does…" and the occasional "help." Nobody gets left at the trailhead.

### Who this is for

**Individuals** who've felt the hundred small impositions and are ready to set the weight down.

**Families** who want their household's data — their kids' photos, their finances, their private life — to stay private, on hardware they control, instead of scattered across a dozen corporate clouds.

**Small organizations** — practices, studios, nonprofits, co-ops — that want infrastructure they own outright, reproducible across every machine in the shop, with no per-seat subscription bleeding them monthly.

**Communities** building toward genuine resilience, who understand that digital sovereignty isn't separate from energy sovereignty or food sovereignty — it's the nervous system that coordinates all the rest.

You do not need to be technical. That's the entire point of hiring a guide. You need only to be *ready* — ready to own your tools instead of renting them.

### The transformation

Strip away the technology and here is what actually changes: you cross from **tenant** to **sovereign.**

A tenant uses tools on someone else's terms, pays rent in attention and data, and can be evicted from features and workflows at the landlord's whim. A sovereign owns the ground, holds the keys, understands the house, and decides which doors open to the world outside.

That crossing changes how it *feels* to sit down at your machine. The low background hum of being watched and monetized goes quiet. In its place is something I can only call **trust** — the earned, inspectable kind, the kind that comes from knowing rather than hoping. Your AI stops being a data-collection funnel wearing a helpful smile and becomes what it should always have been: an instrument of *your* will, on *your* side, computing *your* numbers.

### A note on how I work

Let me be honest about one thing, because it shapes everything else: **this is not a product sale.** I'm not moving units. If you want a slicker version of the same arrangement you already have — a new landlord with a nicer lobby — I'm the wrong person to call.

This is a **values alignment.** I only take on people who actually want what sovereignty costs and what it gives: a little more responsibility in exchange for a great deal more freedom. The work goes well when we agree on *why* before we touch the *how.* So our first conversation isn't a sales pitch. It's a genuine question — is this the direction you want your digital life to go? — and if the answer is no, or not yet, that's a perfectly good answer and we part as friends.

I'd rather help ten people make a crossing they truly wanted than sell a hundred a migration they'll abandon. Sovereignty you don't understand isn't sovereignty; it's just a different cage. So I teach as I build. By the end you won't merely *have* a sovereign machine — you'll *understand* it, well enough to carry it forward on your own. That's the deliverable that matters.

### How to begin

If any of this resonated — if you felt something recognize itself while you were reading — the next step is small and costs you nothing but a conversation.

- **Email me directly:** **raven@peaceengineers.org**
- **Reach me over Nostr**, where I keep my own sovereign presence — the same protocol Peace Protocols federates over.
- **Join the Peace Protocols community** and see the work in the open: the code, the agent constellation, the math, the live dashboard at **[peace-navy.abacusai.cloud](https://peace-navy.abacusai.cloud)**. Everything I've described is real, inspectable, and yours to examine before you ever commit to anything.

We'll start with a conversation about where you are and where you want to go. No obligation, no pressure, no pitch. Just an honest look at whether this crossing is one you want to make — and if it is, a steady hand to help you make it.

I made this journey on an ordinary ZenBook in a quiet room, and it changed how I relate to every machine I touch. I'd be honored to help you make yours.

Welcome to the work of becoming sovereign.

*— Raven Rolland Gregg, Peace Engineers*
