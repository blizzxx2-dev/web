import os as _os
_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), '..', '..'))
import json, re
STEAM=json.load(open(_os.path.join(_os.path.dirname(__file__), 'data', 'steam_games.json')))
G={g['id']:g for g in STEAM if g.get('appid')}

def clean(h):
    h = re.sub(r'<span class="bb_img_ctn">.*?</span>', '', h, flags=re.S)
    h = re.sub(r'<video.*?</video>', '', h, flags=re.S)
    h = re.sub(r'<img[^>]*>', '', h)
    h = re.sub(r'\s(class|style)="[^"]*"', '', h)
    h = re.sub(r'<(\w+)\s+>', r'<\1>', h)
    h = h.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
    h = re.sub(r'<h3>\s*<strong>(.*?)</strong>\s*</h3>', r'<h3>\1</h3>', h, flags=re.S)
    h = re.sub(r'<li>\s*<p>(.*?)</p>\s*</li>', r'<li>\1</li>', h, flags=re.S)
    h = h.replace('&nbsp;', ' ').replace(' ', ' ')
    h = re.sub(r'<(p|h3|li)>\s+', r'<\1>', h)
    h = re.sub(r'\s+</(p|h3|li)>', r'</\1>', h)
    h = re.sub(r'<(p|h3)>\s*</\1>', '', h)
    h = re.sub(r'\s{2,}', ' ', h)
    h = h.replace('&quot;', '"')
    # one block per line
    h = re.sub(r'(</(?:p|h3|li|ul)>)\s*', r'\1\n', h)
    h = h.replace('<ul>', '<ul>\n')
    return h.strip()

FIXES = {
 'engagement': [],
 'fight': [],
 'street-takeover': [
   ('<h3>Two Ways to Play</h3>', '<h3>Two ways to play</h3>'),
   ('<h3>The County Records You</h3>', '<h3>The county records you</h3>'),
   ('<h3>A County Built to Drive</h3>', '<h3>A county built to drive</h3>'),
   ('<h3>Every Mode Covered</h3>', '<h3>Every mode covered</h3>'),
   ('<h3>Built For Your Driving Experience</h3>', '<h3>Built for your driving experience</h3>'),
   ('Persistent Vehicle Damage: Bodywork, Wheels, Suspension, Glass, Engine and Radiator Damage all affect how the car drives.', '<strong>Persistent vehicle damage:</strong> bodywork, wheels, suspension, glass, engine and radiator damage all affect how the car drives.'),
   ('Single-player Campaigns for both Getaway Racers and Police', 'Single-player campaigns for both getaway racers and police'),
   ('Split-Screen Racing and Online Multiplayer', 'Split-screen racing and online multiplayer'),
   ('Free Roam, Time Trial, Drift, Duel, Derby, Elimination and Points Events', 'Free roam, time trial, drift, duel, derby, elimination and points events'),
   ('Keyboard, Gamepad, and Wheel Support with Rebindable Controls', 'Keyboard, gamepad and wheel support with rebindable controls'),
   ('<li>Photo Mode</li>', '<li>Photo mode</li>'),
   ('<li>Driving School</li>', '<li>Driving school</li>'),
 ],
 'mothership': [
   ('<h3>THE STATION IS THE WEAPON</h3>', '<h3>The station is the weapon</h3>'),
   ('<h3>BUILD UNDER FIRE</h3>', '<h3>Build under fire</h3>'),
   ('<h3>BREAK THEM PIECE BY PIECE</h3>', '<h3>Break them piece by piece</h3>'),
   ('<h3>HOLD THE REACH</h3>', '<h3>Hold the Reach</h3>'),
   ('<h3>THE ADMIRALTY REMEMBERS</h3>', '<h3>The Admiralty remembers</h3>'),
   ('<h3>FEATURES</h3>', '<h3>Features</h3>'),
 ],
 'slinghook': [
   ('<p><strong>Eight landscapes to fly through</strong></p>', '<h3>Eight landscapes to fly through</h3>'),
   ('<p><strong>Ways to play</strong></p>', '<h3>Ways to play</h3>'),
   ('<p><strong>And more</strong></p>', '<h3>And more</h3>'),
   ('<p><strong>Built for everyone</strong></p>', '<h3>Built for everyone</h3>'),
 ],
 'phantasm-catalyst': [
   ('<p><strong>Features</strong></p>', '<h3>Features</h3>'),
 ],
 'ace-academy': [
   ('<h3>Read The Table</h3>', '<h3>Read the table</h3>'),
   ('<h3>Catch Them Cheating</h3>', '<h3>Catch them cheating</h3>'),
   ('<h3>Cheat Back</h3>', '<h3>Cheat back</h3>'),
   ('<h3>Fourteen Ways to Gamble, Twenty Rivals</h3>', '<h3>Fourteen ways to gamble, twenty rivals</h3>'),
   ('<h3>Your Choices, Your Ending</h3>', '<h3>Your choices, your ending</h3>'),
 ],
 'field-surgeon': [
   ('<h3>Surgery the way it was done as a Sawdoctor.</h3>', '<h3>Surgery the way a sawdoctor did it.</h3>'),
   ("<h3>Every patient comes from a different culture with it's own</h3>", '<h3>Every patient comes from a different culture, with its own anatomy.</h3>'),
   ('Careful, if The Inquisitor of the Ash Tribunal sees, he would condemn you for witchcraft.', 'Careful: if the Inquisitor of the Ash Tribunal sees it, he will condemn you for witchcraft.'),
   ('<h3>Feature bullets</h3>', '<h3>Features</h3>'),
 ],
}
def about(gid):
    h = clean(G[gid]['about_html'])
    for a,b in FIXES.get(gid, []):
        assert a in h, (gid, a)
        h = h.replace(a,b)
    return h
if __name__=='__main__':
    for gid in G:
        print('=====', gid); print(about(gid))
