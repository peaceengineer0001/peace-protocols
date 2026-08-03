# Migrating an ASUS ZenBook from Windows 11 to NixOS / PeaceOS

*A complete, human-friendly guide to reclaiming your laptop — and installing Peace Protocols on top of it.*

---

## Introduction

If you're reading this, you've probably felt it: the slow creep of a computer that no longer feels like *yours*. Windows 11 asks you to sign in with a Microsoft account before you can even reach the desktop. Updates arrive on someone else's schedule and reboot your machine mid-sentence. Telemetry hums along in the background, quietly narrating your habits to servers you'll never see. The ads have moved into the Start menu. Your files drift into OneDrive whether you asked them to or not.

None of that is an accident. It's the business model.

This guide is about stepping off that treadmill — carefully, with a backup in hand and no drama. We're going to take an ordinary **ASUS ZenBook**, one of the most common ultrabooks in the world, and turn it into a machine that answers to you. The destination is **NixOS**, a Linux distribution unlike any other, dressed up as **PeaceOS** — our opinionated, pre-configured flavor with the **Peace Protocols** agent constellation built in.

### Why NixOS?

Most operating systems are a pile of state that accumulates over years until something breaks and nobody remembers why. NixOS is different in one profound way: **your entire system is described in a single configuration file.** Want to know what's installed, what services run, how your machine is wired together? It's all written down, in plain text, in one place. Change the file, run one command, and your system becomes exactly what the file says — no more, no less.

That gives you three things Windows can never offer:

- **Reproducibility.** The same configuration produces the same system, on this ZenBook or the next one. Your setup becomes a document you can back up, share, and version-control.
- **Atomic upgrades and rollbacks.** Every change is a new "generation." If an update misbehaves, you reboot and pick the previous generation from the boot menu. NixOS quite literally cannot leave you with a half-broken machine.
- **No hidden state.** Nothing gets installed behind your back. Nothing phones home unless you wrote the line that tells it to.

### Why PeaceOS?

PeaceOS is NixOS with a purpose. On top of the rock-solid base we layer **Peace Protocols** — a constellation of 20 AI agents, coordinated by an orchestrator named **Raven**, that help you manage the real dimensions of a sovereign life: your energy, your water, your food, your health, your finances, your community, your knowledge. Underneath the agents runs a **Unified MCP Bus** wiring together 23 integrated tools, with local inference as the primary backend so your thinking doesn't have to leave your laptop.

This guide covers the whole journey: backing up Windows, building the installer, flashing NixOS onto the ZenBook, getting the hardware happy, and finally standing up Peace Protocols so Raven and the council come online.

Take your time. There's no rush, and nothing here is irreversible until the moment you choose to wipe the disk — and we'll flag that moment clearly.

---

## Before You Begin

Gather these before you start. Having everything ready turns a stressful afternoon into a calm one.

- **A USB drive, 8 GB or larger.** It will be completely erased, so use one you don't mind wiping.
- **A backup drive.** An external SSD or a second USB stick large enough to hold your important files. Cloud backup counts too, but a physical copy you control is more in the spirit of the thing.
- **A stable internet connection.** NixOS downloads packages during and after install. Wired Ethernet (via a USB-C adapter) is ideal on a ZenBook, but Wi-Fi is fine.
- **Your ASUS charger, plugged in.** Do not attempt an OS install on battery.
- **About two hours.** The install itself is quick — maybe 30 minutes — but backing up properly and setting things up thoughtfully is where the time goes.
- **A phone or second device.** Handy for reading this guide while your laptop is busy rebooting.

A quiet word before we go further: **an operating system migration wipes the disk.** By the end of Step 4 your Windows installation and everything on it will be gone unless you've backed it up. That's why Step 0 exists, and why it matters more than any other step. Do it thoroughly and the rest is painless.

---

## Step 0: Back Up Windows

Treat this step as sacred. Everything else can be redone; lost files cannot.

**1. Copy your documents and media.** Plug in your backup drive and copy over everything you care about: `Documents`, `Pictures`, `Desktop`, `Downloads`, `Videos`, and any project folders scattered elsewhere. Don't trust your memory — open File Explorer and walk through each library.

**2. Note what's in OneDrive.** ASUS ZenBooks often ship with OneDrive syncing turned on, which means some of your "local" files actually live in the cloud and only *appear* on disk. Open OneDrive, make sure everything has finished syncing (the green checkmarks), and consider using **"Always keep on this device"** so you have real local copies to back up. Anything that lives only in OneDrive will still be in your Microsoft account after migration — but download a copy anyway.

**3. Export your browser data.** In Chrome or Edge, export your **bookmarks** to an HTML file (Bookmarks → Bookmark Manager → Export). If you use the browser's password manager, export those too, or — better — set up a proper password manager like **Bitwarden** or **KeePassXC** now, while you still have Windows, and import everything into it. Both run beautifully on Linux.

**4. Write down your software licenses.** Any paid apps, product keys, or license files you'll want later — collect them in a text file on your backup drive.

**5. Photograph your BIOS settings.** Before you change anything, reboot into the BIOS (we'll cover how in Step 2) and take phone photos of the current settings screens. If you ever want to return the machine to its factory state, these are gold.

**6. Optional: make a Windows recovery drive.** If you think you might want Windows back someday, use Windows' built-in "Create a recovery drive" tool onto a *separate* USB stick. This is entirely optional, but some people sleep better having it.

When your backup drive holds a complete copy of everything that matters, and you've verified you can actually open a few of the copied files, you're ready. Not before.

---

## Step 1: Download the NixOS ISO

Head to the official source — **[nixos.org/download](https://nixos.org/download)** — and never a mirror you found in a random forum.

Choose the **Graphical ISO image** with the **GNOME** desktop. NixOS also offers a Plasma image and a minimal text-only image; GNOME is the friendliest starting point for someone coming from Windows, and it's what PeaceOS assumes by default. You'll download a file named something like `nixos-gnome-24.11-x86_64-linux.iso`.

**Verify the download.** This takes thirty seconds and confirms the file arrived intact and untampered. On the download page, NixOS publishes a **SHA256** checksum next to each image. On Windows, open PowerShell in your Downloads folder and run:

```powershell
Get-FileHash .\nixos-gnome-24.11-x86_64-linux.iso -Algorithm SHA256
```

Compare the printed hash against the one on the website. They should match character for character. If they don't, delete the file and download it again — do not flash a corrupted image.

---

## Step 2: Create a Bootable USB

You'll write the ISO onto your USB drive so the ZenBook can boot from it. Pick whichever method matches the machine you're working on.

**On Windows — Rufus (recommended).** Download **[Rufus](https://rufus.ie)**, a tiny, trusted tool. Insert your USB drive, launch Rufus, and:

- **Device:** your USB drive (double-check the size so you don't wipe the wrong one).
- **Boot selection:** click SELECT and choose the NixOS ISO.
- **Partition scheme:** GPT. **Target system:** UEFI.
- Leave the rest at defaults and click **START**. If Rufus asks about "ISO Image mode vs DD mode," choose **DD mode** for NixOS.

**On a Mac or Linux machine — balenaEtcher.** [Etcher](https://etcher.balena.io) is a clean, cross-platform flasher: select image, select drive, flash. It's hard to get wrong.

**On Linux, the command-line way — `dd`.** If you're comfortable in a terminal, identify your USB device carefully with `lsblk`, then:

```bash
sudo dd if=nixos-gnome-24.11-x86_64-linux.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

Replace `/dev/sdX` with your actual USB device — and be certain, because `dd` will happily overwrite the wrong disk without asking.

### Prepare the ZenBook's BIOS

This is the ASUS-specific part, and it trips people up, so go slowly.

Shut the ZenBook down completely. Then power it on while tapping **F2** repeatedly — that opens the **BIOS / UEFI setup** (ASUS calls it "MyASUS in UEFI" or "Aptio Setup" depending on the model). Press **F7** if you need to switch from the simplified "EZ Mode" into **Advanced Mode**.

Now change three things:

1. **Disable Secure Boot.** Go to the **Security** tab → **Secure Boot** → set to **Disabled**. NixOS can work with Secure Boot, but disabling it for the install avoids a whole category of confusing errors. (You can re-enable it later with extra configuration if you wish.)
2. **Disable Fast Boot.** On the **Boot** tab, turn **Fast Boot** off. This ensures the machine actually checks the USB port at startup.
3. **Confirm USB booting is allowed** and, if present, set the boot mode to **UEFI** (not "Legacy/CSM").

Press **F10** to save and exit. The ZenBook reboots.

---

## Step 3: Boot from the USB

With the NixOS USB inserted, restart the ZenBook and this time tap **Esc** (or **F8** on some ASUS models) to bring up the **one-time boot menu**. You'll see a list of boot devices; choose the one that names your USB drive (often shown as "UEFI: [USB brand]").

If the boot menu doesn't appear, go back into the BIOS (F2), open the **Boot** tab, and move your USB drive to the top of the boot priority list, then save and reboot.

NixOS loads into a live GNOME desktop — a fully working Linux environment running entirely from the USB stick, touching nothing on your disk yet. Take a moment here. Open the Activities overview, move the cursor around, notice that your ZenBook already feels responsive. Nothing you do at this stage is permanent.

Connect to Wi-Fi now using the network icon in the top-right corner, so the installer can fetch the latest packages.

When you're ready, double-click **"Install NixOS"** on the desktop to launch the graphical installer (Calamares).

---

## Step 4: Partition Layout

This is the point of no return, so read the whole section before touching anything.

The installer will ask how you want to use the disk. You have two paths.

### Path A — Single boot (wipe Windows entirely)

This is the clean, recommended choice if you're committing to PeaceOS. Select **"Erase disk"**. The installer proposes a sensible automatic layout, and for most people that's perfect. If you'd like to set it up by hand to match a ZenBook well, here's the layout I use:

| Partition | Size | Type | Mount |
|-----------|------|------|-------|
| EFI System | 512 MB | FAT32 | `/boot` |
| Swap | 32 GB* | linux-swap | — |
| Root | remainder | ext4 or btrfs | `/` |

\* Size swap to match or slightly exceed your RAM if you want reliable hibernation; 16–32 GB is generous for a ZenBook. If you never hibernate, 8 GB is plenty and you can reclaim the rest for root.

**ext4** is boring and bulletproof — a great default. **btrfs** gives you snapshots and compression if you want to experiment later; it pairs nicely with NixOS's rollback philosophy. Either is a fine choice.

### Path B — Dual boot (keep Windows alongside)

If you're not ready to say goodbye to Windows, you can keep both. **Do this from within Windows first:** open Disk Management, right-click your main partition, and **Shrink Volume** to free up at least 60 GB (more is better) of unallocated space. Then boot the NixOS installer and choose **"Install alongside"**, pointing it at that free space. The installer sets up a boot menu that lets you pick Windows or NixOS at startup.

Dual booting is a comfortable on-ramp, but be honest with yourself: many people who "keep Windows just in case" never boot it again. If you've backed up well, Path A is cleaner.

When you've chosen your layout, click through — the installer will show a summary of exactly what it's about to do. **Read it.** This is the last moment Windows still exists. When you're sure, proceed.

---

## Step 5: The NixOS Graphical Install

The rest of the installer is friendly and familiar:

- **Language & region:** pick yours.
- **Timezone:** select on the map or from the list.
- **Keyboard layout:** the ZenBook uses a standard layout; the default usually just works.
- **User account:** choose your name, a username, and a strong password. Tick **"Use the same password for the administrator account"** for simplicity, or set a separate root password if you prefer.
- **Desktop environment:** choose **GNOME**. It's clean, touchpad-friendly, and what PeaceOS builds on.
- **Unfree software:** allow it. This lets NixOS pull in firmware and drivers your ZenBook's Wi-Fi and graphics need.

Click **Install**. Now go make tea. In roughly 20–30 minutes the installer finishes, invites you to **remove the USB drive**, and reboots.

Your ZenBook now boots into NixOS. Windows is gone. The machine is yours.

---

## Step 6: First Boot & Post-Install Essentials

Log in with the username and password you chose. Welcome to GNOME.

**1. Get online.** Click the network icon top-right and connect to Wi-Fi if you're not already.

**2. Meet your configuration.** The single most important file on your new system lives at `/etc/nixos/configuration.nix`. This is the source of truth for your entire machine. Open a terminal (press the Super/Windows key, type "Terminal") and take a look:

```bash
sudo nano /etc/nixos/configuration.nix
```

Everything your system is — its users, its packages, its services — is described here. You don't need to understand all of it yet. Just know that this is where you'll come to change things, and that it's plain text you can back up and re-use forever.

**3. Update the system.** Whenever you edit the configuration, or just want the latest packages, you run one command:

```bash
sudo nixos-rebuild switch
```

This reads your configuration, builds the exact system it describes, and switches to it — creating a new generation you can roll back to. Run it now to pull any updates that landed since the ISO was built.

**4. Confirm the ZenBook hardware is happy.** Walk through the basics:

- **Touchpad** — two-finger scroll, tap-to-click. GNOME's Settings → Mouse & Touchpad exposes the options.
- **Function keys** — brightness (Fn+F7/F8 on most ZenBooks), volume, keyboard backlight.
- **Webcam** — open the Cheese app (or Settings) to confirm it lights up.
- **Battery** — the top-right menu should show a charge percentage.

Most ZenBooks work fully out of the box with a current NixOS release. If something's off, the **Troubleshooting** section near the end has ASUS-specific fixes.

---

## Step 7: Install Peace Protocols

Now the part you came for. We'll bring the Peace Protocols agent constellation online.

**1. Install git and clone the repository.** Add `git` to your configuration (under `environment.systemPackages`) and rebuild, or grab it temporarily for this session:

```bash
nix-shell -p git python3
git clone https://github.com/peaceengineer0001/peace-protocols.git
cd peace-protocols
```

**2. Set up the Python environment and dependencies.** Peace Protocols ships a consolidated `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .          # installs the mcp_bus, integrations, and math packages
```

**3. Validate the MCP registry.** Before starting anything, confirm the 23-server registry parses cleanly:

```bash
python3 scripts/validate_mcp_registry.py
# Expected: Loaded 23 servers (6 native, 17 adapters) — 0 error(s)
```

**4. Bring the Unified MCP Bus up.** This is the backbone that connects every agent to every tool:

```bash
python3 -m mcp_bus.serve --once     # brings the bus up and prints a health report
```

You'll see each server's status as the connection pool starts them concurrently. Servers whose upstream service isn't provisioned yet (a GPU inference daemon, an external API key) will report as offline — that's expected on a fresh machine. The bus isolates faults so one missing service never takes down the rest.

### The NixOS-native way (recommended)

Because this is NixOS, there's a cleaner path than a virtualenv: declare Peace Protocols as part of your system using the provided **flake**. The repo's `nixos/` directory contains a `flake.nix` and six modules — `peace-protocols`, `mcp-bus`, `inference`, `voice`, `intel`, and `commerce`.

```bash
cd nixos
# Inspect the flake and the PeaceOS system definition
nix flake show

# Build and switch your whole system to the PeaceOS configuration
sudo nixos-rebuild switch --flake .#peaceos
```

This wires the MCP Bus in as a proper **systemd service** that starts on boot, pulls in the right dependencies declaratively, and makes your entire Peace Protocols setup reproducible. From now on, your sovereign operating system is described in code — copy the flake to a new ZenBook and you get the identical environment.

To enable only the pieces you want, edit the module imports in the flake and toggle options like `services.peace-protocols.mcp-bus.enable` or `services.peace-protocols.inference.enable`, then rebuild. Every capability is opt-in.

---

## Step 8: Configure Your Agent Constellation

Peace Protocols is organized as a **constellation of 20 agents**, each responsible for one dimension of a sovereign life. Their configurations live under `agents/`, one directory per agent, each with a `config.toml`, a system prompt, and intake questions.

At the center is **Raven** — the master orchestrator, agent #20. Raven doesn't do domain work directly; Raven *coordinates*. It runs the weekly synthesis, calculates the two master metrics (the Peace Efficiency Index, **Pe**, and the Community Vitality Index, **CVI**), and drives the 6D loop across every other agent.

Raven coordinates two groups:

- **Seven Sovereign Bodies** — Starfire, Sage, River, Stone, Ember, Cedar, and Summit — the governance-and-wellbeing layer.
- **Twelve Resource Realms** — Sol (energy), Tide (water), Root (food), Heal (health), Haven (shelter), Cycle (waste), Lore (knowledge), Mesh (communication), Passage (transport), Forge (manufacturing), Thrive (economics), and Council (governance) — each tracking a concrete self-sufficiency ratio.

Open any agent to see how it's wired:

```bash
cat agents/sol/config.toml       # the Energy realm agent
cat agents/raven/config.toml     # the orchestrator
```

To activate an agent, set `enabled = true` in its `config.toml`, choose the model it should use, and adjust its privacy tier (1 = local only, up to 4 = federated aggregate). Start small — bring up Raven and one or two realms that matter most to you, get comfortable with the weekly report, then widen the constellation as you go. There's no prize for turning everything on at once.

---

## Step 9: Connect to the Buzz Agentic Harness

Peace Protocols is not a standalone island — it's an **overlay** on top of **Buzz**, an agentic harness built on the Nostr protocol. If NixOS is the sovereign body of your machine, Buzz is its nervous system for talking to the wider world without surrendering to a central authority.

In plain terms: **Nostr** is a simple, censorship-resistant messaging protocol where your identity is a cryptographic keypair you own — not an account a company can suspend. **Buzz** uses Nostr relays as the substrate over which agents coordinate, publish signed events, and sync state. Peace Protocols layers its agent constellation and MCP Bus on top, so Raven and the council can operate locally *and* participate in a federation of other sovereign nodes when you choose to.

Each agent has an `[mcp]` section pointing at a relay endpoint (`ws://localhost:4736` by default) authenticated with **NIP-42**. On first run you'll generate your Nostr keypair — **guard the private key like the keys to your house**, because it *is* your identity across the entire network. The privacy tiers you set in Step 8 decide what, if anything, ever leaves your laptop: by default, everything stays local, and only aggregates you explicitly promote are shared upward.

You don't need to master Nostr to use PeaceOS. Just understand the shape of it: **you own your keys, your data stays yours by default, and federation is a choice you make deliberately — never a default someone imposed on you.**

---

## Troubleshooting (ASUS ZenBook specifics)

Most ZenBooks run NixOS beautifully. When something needs a nudge, it's usually one of these.

**Wi-Fi not detected.** Newer ZenBooks use **Intel AX-series** Wi-Fi cards (AX201, AX211) that need firmware. Make sure you allowed unfree software during install. If Wi-Fi is still missing, enable firmware in your configuration and rebuild:

```nix
hardware.enableAllFirmware = true;
hardware.enableRedistributableFirmware = true;
```

Then `sudo nixos-rebuild switch`. If you're stuck with no network at all, tether over USB from your phone to get online for that first rebuild.

**Touchpad gestures feel off.** NixOS uses **libinput**, which handles ZenBook touchpads well. Fine-tune in GNOME Settings → Mouse & Touchpad (natural scrolling, tap-to-click). For per-detail control you can add libinput options to your configuration.

**Brightness keys don't work.** A common ASUS quirk. Add a kernel parameter to your configuration:

```nix
boot.kernelParams = [ "acpi_backlight=native" ];
```

Rebuild and reboot. If that doesn't do it, try `acpi_backlight=vendor` instead.

**Sleep / suspend problems.** Some ZenBook models ship with "modern standby" (S0ix) that Linux handles unevenly, occasionally draining battery in the bag. Check your BIOS for a sleep-state option and prefer **S3** if it's offered. Test suspend deliberately (close the lid, wait, reopen) before trusting it on a trip.

**Function-key row does nothing.** ASUS laptops toggle between function keys and media keys with **Fn + Esc**. If your F-keys behave unexpectedly, try that toggle first.

**The machine won't boot from USB at all.** Return to the BIOS, re-confirm **Secure Boot is disabled** and **Fast Boot is off**, and that the boot mode is **UEFI**. Ninety percent of "it won't boot" reports trace back to one of these three.

When you're truly stuck, the NixOS community is unusually warm and technical — the [NixOS Discourse](https://discourse.nixos.org) and the wiki are excellent, and a search for "ZenBook [your model] NixOS" often turns up someone who's already solved it.

---

## What's Next

You did it. Windows is behind you, PeaceOS is your foundation, and Raven is watching over a constellation that works for you instead of on you.

Here's where to go from here:

- **Read the v2 upgrade guide** — `docs/v2-upgrade.md` in the repo — to understand the full Agent Zero capability layer and how the 23 integrations fit together.
- **Review the license posture** — `docs/LICENSE-COMPLIANCE.md` — so you know which integrations are consent-gated (like Heretic) or non-commercial (like GHOST).
- **Explore the math** — the `math/` directory holds the real calculators behind Pe, CVI, and the 19 domain indexes. They're readable Python; run them and watch your own numbers.
- **Watch the live dashboard** at **[peace-navy.abacusai.cloud](https://peace-navy.abacusai.cloud)** to see the constellation, the bus, and the calculators in action.
- **Version-control your configuration.** Put `/etc/nixos/` and your PeaceOS flake into a private git repo. Your entire sovereign machine becomes a document you can restore, clone, and evolve.

One last thought. The goal of all this was never Linux for its own sake. It was **sovereignty** — the quiet confidence of using a machine that keeps your secrets, obeys your intentions, and can be understood all the way down. NixOS gives you a body that never rots. Peace Protocols gives it a mind that serves you. From here, the direction is yours to choose.

Welcome home.

---

*Questions, or want a hand with your own migration? Reach out at **raven@peaceengineers.org** or find us in the Peace Protocols community. We help people make exactly this journey — see the companion document, "From Windows Tenant to Digital Sovereign."*
