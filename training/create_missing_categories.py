#!/usr/bin/env python3
"""
Create Comprehensive Missing AAC Categories
Fill all the gaps in our AAC communication coverage
"""
import json

def create_missing_categories():
    """Create all missing AAC communication categories"""
    
    print("🌟 TinkyBink Missing Categories Creator")
    print("=" * 60)
    print("🚀 Creating ALL missing AAC categories")
    print("💯 Comprehensive communication coverage")
    print()
    
    all_new_examples = []
    
    # HIGH PRIORITY CATEGORIES
    categories_created = []
    
    # 1. Healthcare Navigation (20 examples)
    healthcare_examples = create_healthcare_navigation()
    all_new_examples.extend(healthcare_examples)
    categories_created.append(f"Healthcare Navigation: {len(healthcare_examples)} examples")
    
    # 2. Legal/Government (15 examples)
    legal_examples = create_legal_government()
    all_new_examples.extend(legal_examples) 
    categories_created.append(f"Legal/Government: {len(legal_examples)} examples")
    
    # 3. Entertainment/Media (20 examples)
    entertainment_examples = create_entertainment_media()
    all_new_examples.extend(entertainment_examples)
    categories_created.append(f"Entertainment/Media: {len(entertainment_examples)} examples")
    
    # 4. Home Management (18 examples)
    home_examples = create_home_management()
    all_new_examples.extend(home_examples)
    categories_created.append(f"Home Management: {len(home_examples)} examples")
    
    # 5. Crisis Management (15 examples)
    crisis_examples = create_crisis_management()
    all_new_examples.extend(crisis_examples)
    categories_created.append(f"Crisis Management: {len(crisis_examples)} examples")
    
    # 6. Parenting/Childcare (18 examples)
    parenting_examples = create_parenting_childcare()
    all_new_examples.extend(parenting_examples)
    categories_created.append(f"Parenting/Childcare: {len(parenting_examples)} examples")
    
    # 7. Goal Setting (12 examples)
    goals_examples = create_goal_setting()
    all_new_examples.extend(goals_examples)
    categories_created.append(f"Goal Setting: {len(goals_examples)} examples")
    
    # MEDIUM PRIORITY CATEGORIES
    
    # 8. Dining/Restaurants (15 examples)
    dining_examples = create_dining_restaurants()
    all_new_examples.extend(dining_examples)
    categories_created.append(f"Dining/Restaurants: {len(dining_examples)} examples")
    
    # 9. Travel/Vacation (15 examples)
    travel_examples = create_travel_vacation()
    all_new_examples.extend(travel_examples)
    categories_created.append(f"Travel/Vacation: {len(travel_examples)} examples")
    
    # 10. Health/Fitness (12 examples)
    fitness_examples = create_health_fitness()
    all_new_examples.extend(fitness_examples)
    categories_created.append(f"Health/Fitness: {len(fitness_examples)} examples")
    
    # 11. Events/Celebrations (12 examples)
    events_examples = create_events_celebrations()
    all_new_examples.extend(events_examples)
    categories_created.append(f"Events/Celebrations: {len(events_examples)} examples")
    
    # 12. Banking/Finance (12 examples)
    banking_examples = create_banking_finance()
    all_new_examples.extend(banking_examples)
    categories_created.append(f"Banking/Finance: {len(banking_examples)} examples")
    
    # 13. Neighborhood/Community (10 examples)
    community_examples = create_neighborhood_community()
    all_new_examples.extend(community_examples)
    categories_created.append(f"Neighborhood/Community: {len(community_examples)} examples")
    
    # 14. Pets/Animals (10 examples)
    pets_examples = create_pets_animals()
    all_new_examples.extend(pets_examples)
    categories_created.append(f"Pets/Animals: {len(pets_examples)} examples")
    
    # LOWER PRIORITY CATEGORIES
    
    # 15. Gaming/Sports (10 examples)
    gaming_examples = create_gaming_sports()
    all_new_examples.extend(gaming_examples)
    categories_created.append(f"Gaming/Sports: {len(gaming_examples)} examples")
    
    # 16. DIY/Crafts (8 examples)
    diy_examples = create_diy_crafts()
    all_new_examples.extend(diy_examples)
    categories_created.append(f"DIY/Crafts: {len(diy_examples)} examples")
    
    # 17. News/Current Events (8 examples)
    news_examples = create_news_current_events()
    all_new_examples.extend(news_examples)
    categories_created.append(f"News/Current Events: {len(news_examples)} examples")
    
    # 18. Future Planning (8 examples)
    future_examples = create_future_planning()
    all_new_examples.extend(future_examples)
    categories_created.append(f"Future Planning: {len(future_examples)} examples")
    
    total_new = len(all_new_examples)
    
    print(f"📊 CATEGORIES CREATED:")
    for category in categories_created:
        print(f"   ✅ {category}")
    
    print(f"\n🎯 TOTAL NEW EXAMPLES: {total_new:,}")
    
    # Save all missing categories
    output_file = "tinkybink_missing_categories_complete.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in all_new_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved: {output_file}")
    print(f"🏆 AAC coverage now COMPREHENSIVE!")
    
    return total_new

def create_healthcare_navigation():
    """Healthcare/medical navigation examples"""
    examples = []
    
    scenarios = [
        ("Need to schedule doctor appointment", "📞 Call doctor's office, 📅 Check available dates, 🏥 Urgent care instead, 💻 Online scheduling portal", "healthcare"),
        ("Insurance won't cover treatment", "📞 Call insurance company, 📋 Get prior authorization, 💰 Pay out pocket, 🏥 Find covered provider", "healthcare"),
        ("Which specialist do I need?", "🩺 Ask primary doctor, 📱 Check insurance directory, 🔍 Research symptoms online, 🤝 Get second opinion", "healthcare"),
        ("Prescription is too expensive", "💊 Ask generic version, 💰 Check discount programs, 📋 Insurance formulary review, 🏥 Different medication option", "healthcare"),
        ("Medical test results confusing", "🩺 Call doctor explain, 📋 Request written summary, 🔍 Research terms online, 👥 Bring family meeting", "healthcare"),
        ("Hospital bill is wrong", "📞 Call billing department, 📋 Request itemized bill, 💳 Payment plan option, 🤝 Patient advocate help", "healthcare"),
        ("Need medical records transferred", "📋 Request records form, 📧 Electronic transfer option, 📠 Fax to provider, 💾 Get copies myself", "healthcare"),
        ("Emergency room or urgent care?", "🚨 Life threatening emergency, 🏥 Urgent care sufficient, 📞 Call doctor first, 🚑 Ambulance if severe", "healthcare"),
        ("Second opinion on diagnosis", "🩺 Find another specialist, 📋 Get records copied, 💰 Check insurance coverage, 🔍 Research condition more", "healthcare"),
        ("Physical therapy not helping", "🏥 Talk to therapist, 🩺 Consult prescribing doctor, 💪 Try different exercises, ⏰ Give more time", "healthcare"),
        ("Medication side effects concern", "🩺 Call doctor immediately, 💊 Read medication guide, 📋 Document side effects, 🚨 Emergency if severe", "healthcare"),
        ("Can't afford medical treatment", "💰 Ask payment plans, 🏥 Check charity programs, 📋 Apply financial aid, 🤝 Social worker help", "healthcare"),
        ("Long wait for appointment", "📞 Call for cancellations, 🏥 Try different provider, 🚨 Urgent care meanwhile, 📅 Wait list option", "healthcare"),
        ("Medical form too complicated", "🤝 Ask staff help, 👥 Bring family member, 📋 Take home complete, 💻 Online form easier", "healthcare"),
        ("Doctor doesn't listen well", "📝 Write questions beforehand, 🗣️ Be more assertive, 👥 Bring advocate along, 🏥 Find different doctor", "healthcare"),
        ("Health insurance confusing", "📞 Call member services, 📖 Read benefits summary, 🤝 Insurance navigator help, 💻 Online portal tutorial", "healthcare"),
        ("Medical emergency while traveling", "🚨 Call 911 immediately, 🏥 Nearest emergency room, 📱 Call travel insurance, 📋 Medical ID information", "healthcare"),
        ("Chronic condition management overwhelming", "📚 Patient education classes, 🤝 Support group join, 📱 Health tracking apps, 🩺 Care coordinator help", "healthcare"),
        ("Preventive care screening due", "📅 Schedule annual physical, 🔍 Check recommended screenings, 📋 Insurance coverage verify, 🏥 Women's health exam", "healthcare"),
        ("Mental health resources needed", "🧠 Find therapist nearby, 📞 Crisis hotline number, 💊 Psychiatric medication evaluation, 🤝 Support group options", "healthcare")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Healthcare Navigation",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_legal_government():
    """Legal and government services examples"""
    examples = []
    
    scenarios = [
        ("Need legal advice urgently", "⚖️ Call lawyer immediately, 📞 Legal aid society, 💰 Free consultation available, 📚 Research legal options", "legal"),
        ("Government benefits application", "📋 Complete application forms, 📞 Call benefits office, 💻 Apply online portal, 🤝 Get application help", "legal"),
        ("Voting information needed", "🗳️ Check voter registration, 📍 Find polling location, 📅 Early voting options, 📧 Absentee ballot request", "legal"),
        ("Social Security card lost", "📋 Replacement card application, 💻 Online SSA account, 📞 Call Social Security, 🏢 Visit local office", "legal"),
        ("Taxes are too complicated", "💰 Hire tax preparer, 💻 Tax software help, 📚 Free tax assistance, 📋 Organize tax documents", "legal"),
        ("Discrimination at work", "📋 File complaint HR, ⚖️ Contact EEOC office, 📞 Employment lawyer consult, 📝 Document everything carefully", "legal"),
        ("Landlord tenant dispute", "📋 Know tenant rights, ⚖️ Contact tenant union, 📞 Legal aid help, 📝 Document lease violations", "legal"),
        ("Identity theft occurred", "📞 Call credit bureaus, 👮 File police report, 💳 Contact bank immediately, 📋 Identity theft affidavit", "legal"),
        ("Immigration status questions", "⚖️ Immigration lawyer needed, 📞 Legal aid services, 📋 USCIS information website, 🤝 Community organization help", "legal"),
        ("Child custody issues", "⚖️ Family law attorney, 📋 Court mediation services, 📞 Legal aid family, 📝 Document child's interests", "legal"),
        ("Small claims court filing", "📋 Small claims forms, 💰 Filing fee required, 📅 Court date scheduled, 📝 Organize evidence documents", "legal"),
        ("Power of attorney needed", "⚖️ Estate planning lawyer, 📋 POA forms available, 💰 Notary public required, 👥 Family discussion first", "legal"),
        ("Traffic ticket dispute", "⚖️ Contest in court, 💰 Pay fine online, 📚 Traffic school option, 📞 Lawyer for serious", "legal"),
        ("Bankruptcy consideration", "⚖️ Bankruptcy attorney consultation, 💰 Credit counseling first, 📋 Financial documents needed, 🤝 Debt management alternatives", "legal"),
        ("Public records request", "📋 FOIA request form, 📞 Government office call, 💰 Processing fees apply, ⏰ Response time varies", "legal")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Legal Government",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_entertainment_media():
    """Entertainment and media examples"""
    examples = []
    
    scenarios = [
        ("What should we watch tonight?", "🎬 New movie release, 📺 Favorite TV series, 🎭 Comedy show special, 🎵 Music documentary film", "entertainment"),
        ("This music is amazing", "🎵 Love this artist, 🎧 Add to playlist, 💿 Buy the album, 🎤 Learn the lyrics", "entertainment"),
        ("Social media is overwhelming", "📱 Take a break, 🔇 Mute negative content, 👥 Unfollow toxic accounts, ⏰ Limit screen time", "entertainment"),
        ("Streaming service recommendations", "🎬 Netflix has variety, 📺 Hulu good shows, 🎭 Amazon Prime movies, 💰 Free options available", "entertainment"),
        ("Concert tickets available", "🎵 Buy tickets now, 💰 Check ticket prices, 📅 Concert date works, 👥 Who else going", "entertainment"),
        ("Book recommendation needed", "📚 What genre prefer, ⭐ Check bestseller lists, 👥 Ask friends suggestions, 📖 Library has copies", "entertainment"),
        ("Video game night", "🎮 What game play, 👥 Multiplayer options available, 🏠 Host at place, 🍕 Order pizza tonight", "entertainment"),
        ("Podcast discovery", "🎧 What topics interest, ⭐ Check popular lists, 📱 Download podcast app, ⏰ Listen during commute", "entertainment"),
        ("Art museum visit", "🎨 Special exhibit showing, 📅 Museum hours today, 💰 Admission price check, 🎧 Audio tour available", "entertainment"),
        ("Theater show tickets", "🎭 Broadway show available, 💰 Check ticket prices, 📅 Show times tonight, 👥 Group discount available", "entertainment"),
        ("Sports game on TV", "⚽ What game tonight, 📺 Which channel showing, 👥 Watch party planned, 🍿 Get snacks ready", "entertainment"),
        ("Celebrity news gossip", "⭐ Interesting celebrity news, 📱 Social media updates, 📺 Entertainment news show, 🤔 Take with grain", "entertainment"),
        ("Photography hobby", "📸 New camera gear, 🌅 Good lighting today, 👥 Photography class available, 📱 Edit photos app", "entertainment"),
        ("Dance class interest", "💃 What dance style, 📅 Class schedule times, 💰 Lesson prices check, 👥 Partner needed maybe", "entertainment"),
        ("Comedy club night", "😂 Stand up comedy, 🎭 Local comedy club, 💰 Ticket prices tonight, 👥 Go with friends", "entertainment"),
        ("Karaoke party", "🎤 Song requests ready, 🎵 Popular karaoke songs, 😊 Don't mind singing, 👥 Group karaoke fun", "entertainment"),
        ("Board game collection", "🎲 New board games, 👥 Game night friends, 🏠 Host game night, 📚 Learn new rules", "entertainment"),
        ("Magazine subscription", "📖 What magazines interest, 💰 Subscription prices compare, 📱 Digital version available, 📚 Library has copies", "entertainment"),
        ("Film festival tickets", "🎬 Independent films showing, 🎭 Documentary film festival, 📅 Festival schedule check, 🎫 Early bird discounts", "entertainment"),
        ("Online content creation", "💻 Start YouTube channel, 📱 Social media content, 🎨 Creative content ideas, 👥 Build audience slowly", "entertainment")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Entertainment Media",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_home_management():
    """Home management examples"""
    examples = []
    
    scenarios = [
        ("House cleaning overwhelmed", "🧹 Hire cleaning service, 📅 Create cleaning schedule, 🤝 Family help needed, 🏠 Focus one room", "home_management"),
        ("Utility bill too high", "💡 Energy efficient appliances, 🌡️ Adjust thermostat settings, 📞 Call utility company, 💰 Budget payment plan", "home_management"),
        ("Home repair needed", "🔧 Call repair person, 💻 YouTube tutorial help, 🛠️ Hardware store advice, 💰 Get multiple quotes", "home_management"),
        ("Pest control problem", "🐛 Call exterminator service, 🏠 Seal entry points, 🧹 Deep clean areas, 💰 Natural pest solutions", "home_management"),
        ("Garden maintenance", "🌱 Plant seasonal flowers, 💧 Watering schedule needed, 🔧 Garden tools required, 🤝 Landscaping service help", "home_management"),
        ("Home security concerns", "🔒 Install security system, 💡 Motion sensor lights, 📞 Neighborhood watch group, 🏠 Check locks regularly", "home_management"),
        ("Internet wifi problems", "📞 Call internet provider, 🔄 Restart router modem, 📍 Check wifi coverage, 💻 Upgrade internet plan", "home_management"),
        ("Appliance not working", "🔧 Check warranty coverage, 📞 Call repair service, 💻 Troubleshooting guide online, 🛒 Replacement appliance cost", "home_management"),
        ("Home organization project", "📦 Declutter room systematically, 🛒 Storage solutions needed, 📅 Set organization goals, 👥 Professional organizer help", "home_management"),
        ("Property tax bill", "💰 Budget for payment, 📞 Appeal assessment value, 📅 Payment due date, 🏛️ County assessor office", "home_management"),
        ("Neighborhood noise complaint", "📞 Talk to neighbors, 🏛️ Contact city code, 📝 Document noise incidents, ⏰ Noise ordinance hours", "home_management"),
        ("Home insurance review", "📋 Compare insurance quotes, 💰 Coverage amounts adequate, 📞 Agent review policy, 🏠 Home value updated", "home_management"),
        ("Moving preparation", "📦 Start packing early, 🚚 Moving company quotes, 📅 Change address everywhere, 🏠 Utility transfer dates", "home_management"),
        ("Emergency preparedness", "🔦 Emergency kit supplies, 💧 Water storage ready, 📻 Battery powered radio, 📋 Emergency contact list", "home_management"),
        ("Home improvement project", "🏠 Contractor estimates needed, 💰 Budget for project, 📅 Timeline for completion, 🔧 DIY or professional", "home_management"),
        ("Garbage disposal issues", "🔧 Call plumber service, 💻 Reset disposal switch, 🧹 Clean disposal thoroughly, 🛒 Replacement disposal cost", "home_management"),
        ("Smoke detector beeping", "🔋 Replace battery immediately, 🔥 Test smoke detector, 📞 Fire department inspection, 🏠 Carbon monoxide detector", "home_management"),
        ("Yard sale preparation", "🏷️ Price items fairly, 📅 Advertise yard sale, 💰 Make change ready, 📦 Organize items categories", "home_management")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Home Management",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_crisis_management():
    """Crisis and mental health management examples"""
    examples = []
    
    scenarios = [
        ("Having panic attack right now", "🫁 Deep breathing exercises, 📞 Call crisis hotline, 🤝 Safe person nearby, 🏥 Emergency room if", "crisis"),
        ("Feeling suicidal thoughts", "📞 988 suicide hotline, 🏥 Emergency room immediately, 🤝 Trusted person tell, 👮 Police welfare check", "crisis"),
        ("Substance abuse relapse", "📞 Sponsor or counselor, 🏥 Detox program needed, 👥 Support group meeting, 🤝 Family member help", "crisis"),
        ("Domestic violence situation", "📞 Domestic violence hotline, 👮 Police report incident, 🏠 Safe shelter location, 📋 Safety plan create", "crisis"),
        ("Mental health crisis", "📞 Crisis mental health, 🏥 Psychiatric emergency room, 💊 Medication adjustment needed, 🤝 Emergency contact person", "crisis"),
        ("Child abuse suspected", "📞 Child protective services, 👮 Police report immediately, 🏥 Medical exam needed, 📋 Document evidence carefully", "crisis"),
        ("Financial crisis emergency", "📞 Financial counseling service, 🏛️ Social services help, 💰 Emergency assistance programs, 🤝 Family support system", "crisis"),
        ("Addiction intervention needed", "🤝 Professional interventionist help, 👥 Family support group, 🏥 Treatment program research, 📞 Addiction counselor consult", "crisis"),
        ("Elder abuse concern", "📞 Adult protective services, 👮 Police welfare check, 🏥 Medical evaluation needed, 📋 Document abuse signs", "crisis"),
        ("Homelessness imminent", "🏠 Homeless shelter contact, 🏛️ Housing assistance programs, 📞 Social services help, 👥 Community resources available", "crisis"),
        ("Sexual assault occurred", "📞 RAINN hotline support, 👮 Police report option, 🏥 Medical exam rape, 🤝 Trusted support person", "crisis"),
        ("Severe depression episode", "📞 Crisis counselor call, 💊 Medication evaluation urgent, 🤝 Support system activate, 🏥 Psychiatric hospitalization consider", "crisis"),
        ("Eating disorder relapse", "📞 Eating disorder hotline, 🏥 Medical evaluation needed, 👥 Support group meeting, 🤝 Treatment team contact", "crisis"),
        ("Self harm urges", "📞 Crisis text line, 🤝 Safe person call, 🏥 Emergency mental health, 📋 Safety plan review", "crisis"),
        ("Trauma flashbacks severe", "🫁 Grounding techniques use, 📞 Trauma therapist call, 💊 Medication for anxiety, 🤝 Trusted person nearby", "crisis")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()} right now."
        
        example = {
            "instruction": "AAC Crisis Management",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_parenting_childcare():
    """Parenting and childcare examples"""
    examples = []
    
    scenarios = [
        ("Child having behavioral problems", "👶 Consistent discipline approach, 📚 Parenting class help, 🤝 Child psychologist consult, 📅 Reward system try", "parenting"),
        ("Teenager not listening", "💬 Open communication important, 📱 Set clear boundaries, 🤝 Family counseling help, ⏰ Choose battles wisely", "parenting"),
        ("School academic struggles", "📚 Extra tutoring help, 👩‍🏫 Teacher conference meeting, 🧠 Learning disability evaluation, 📅 Study schedule create", "parenting"),
        ("Childcare provider needed", "👶 Daycare center research, 🤝 Nanny background check, 👥 Family member help, 💰 Childcare costs budget", "parenting"),
        ("Child health concerns", "🩺 Pediatrician appointment schedule, 🏥 Urgent care visit, 📋 Growth chart tracking, 💊 Medication compliance check", "parenting"),
        ("Potty training struggles", "👶 Stay patient consistent, 📚 Potty training books, 🎁 Reward system use, ⏰ Child's readiness important", "parenting"),
        ("Sibling rivalry constant", "👶 Individual attention needed, 📚 Sibling relationship books, 🤝 Family counseling help, 📅 Special time each", "parenting"),
        ("Child won't sleep", "😴 Bedtime routine consistent, 📚 Sleep training methods, 🩺 Pediatrician advice ask, 🤝 Sleep consultant help", "parenting"),
        ("Picky eater child", "🍎 Offer variety foods, 👩‍🍳 Involve cooking preparation, 🩺 Nutritionist consult if, 🍽️ Family meal together", "parenting"),
        ("Screen time concerns", "📱 Set device limits, 📚 Educational content choose, ⏰ Screen free times, 🎨 Alternative activities offer", "parenting"),
        ("Bullying at school", "👩‍🏫 Talk to teacher, 📞 Principal meeting request, 👶 Role play responses, 🤝 Counselor support needed", "parenting"),
        ("Child development milestones", "👶 Track development progress, 📚 Milestone chart reference, 🩺 Pediatrician discuss concerns, 🎯 Early intervention services", "parenting"),
        ("Homework battles", "📚 Create homework space, ⏰ Set homework schedule, 🎁 Reward system implement, 🤝 Tutor help consider", "parenting"),
        ("Teenage dating concerns", "💬 Open honest communication, 📚 Relationship education discuss, 🚗 Transportation safety rules, ⏰ Curfew boundaries set", "parenting"),
        ("Child anxiety issues", "🧠 Child therapist find, 💊 Anxiety medication consider, 📚 Anxiety coping strategies, 🤝 Support group parents", "parenting"),
        ("Single parenting overwhelming", "🤝 Single parent support, 👥 Family help ask, 📅 Self care important, 💰 Financial assistance resources", "parenting"),
        ("College preparation", "📚 SAT ACT prep, 💰 College savings plan, 📋 Application timeline create, 🎯 Career counseling help", "parenting"),
        ("Child safety online", "💻 Parental controls set, 📚 Internet safety education, 📱 Monitor online activity, 🚨 Report inappropriate content", "parenting")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"My child needs {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Parenting Childcare",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_goal_setting():
    """Goal setting and achievement examples"""
    examples = []
    
    scenarios = [
        ("Want to set life goals", "🎯 Write specific goals, 📅 Set realistic timeline, 📋 Break into steps, 📊 Track progress regularly", "goals"),
        ("Motivation is lacking", "💪 Remember your why, 👥 Find accountability partner, 🎁 Reward small wins, 📚 Read motivational content", "goals"),
        ("Goal seems too big", "📋 Break into steps, 🎯 Focus on next, ⏰ Set smaller milestones, 🤝 Get support help", "goals"),
        ("Made progress today", "🎉 Celebrate the achievement, 📊 Track progress made, 💪 Keep momentum going, 📅 Plan tomorrow's action", "goals"),
        ("Stuck on current goal", "🤔 Reassess the approach, 🤝 Ask for help, 📚 Learn new strategies, 🔄 Adjust goal if", "goals"),
        ("Career advancement goal", "📚 Skill development plan, 👥 Network building important, 💼 Performance improvement focus, 🎯 Promotion timeline realistic", "goals"),
        ("Health fitness goal", "🏋️ Exercise routine start, 🍎 Nutrition plan create, 📊 Progress tracking important, 🤝 Workout partner help", "goals"),
        ("Financial savings goal", "💰 Budget plan create, 📊 Track spending habits, 🎯 Savings target realistic, 📅 Automatic savings setup", "goals"),
        ("Learning new skill", "📚 Online course enroll, ⏰ Practice time schedule, 🎯 Skill level goals, 🤝 Study group join", "goals"),
        ("Relationship improvement goal", "💬 Communication skills improve, ⏰ Quality time schedule, 🎁 Thoughtful gestures make, 📚 Relationship books read", "goals"),
        ("Procrastination problem", "📅 Deadline accountability create, 🎯 Start with tasks, ⏰ Time blocking method, 🎁 Reward completion tasks", "goals"),
        ("Long term vision", "🌟 Dream big picture, 📅 Five year plan, 🎯 Annual goals set, 📋 Monthly action steps", "goals")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Goal Setting",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with medium priority categories...

def create_dining_restaurants():
    """Dining and restaurant examples"""
    examples = []
    
    scenarios = [
        ("What looks good on menu?", "🍝 Pasta dish sounds, 🥗 Salad looks fresh, 🍔 Burger with fries, 🐟 Fish special today", "dining"),
        ("Any food allergies tonight?", "🥜 Allergic to nuts, 🥛 Lactose intolerant dairy, 🦐 Shellfish allergy severe, ✅ No allergies here", "dining"),
        ("Ready to order now?", "✅ Yes ready order, ⏰ Need few minutes, ❓ What do recommend, 👥 Others still deciding", "dining"),
        ("How was everything tonight?", "😋 Food was delicious, 👍 Service was excellent, 😐 It was okay, 🤔 Could be better", "dining"),
        ("Dessert menu interest you?", "🍰 Dessert sounds great, ☕ Just coffee please, 🍨 Ice cream option, ❌ Too full tonight", "dining"),
        ("Separate checks or together?", "💳 All on card, 💰 Split the bill, 👥 Separate checks please, 💸 I'll pay tonight", "dining"),
        ("Reservation for how many?", "👥 Table for two, 👨‍👩‍👧‍👦 Family of four, 👥 Large group eight, 📞 Call ahead reservation", "dining"),
        ("Wine pairing recommendation?", "🍷 Red wine please, 🥂 White wine better, 🍺 Beer instead tonight, 💧 Just water tonight", "dining"),
        ("Spice level preference?", "🌶️ Extra spicy please, 🔥 Medium heat good, 😌 Mild spice level, ❌ No spice please", "dining"),
        ("Takeout or dining in?", "🏠 Takeout to go, 🍽️ Dining in tonight, 🚗 Curbside pickup ready, 📱 Delivery to home", "dining"),
        ("Happy hour specials?", "🍻 Drink specials available, 🍤 Appetizer half price, ⏰ Until 6 PM, 💰 Good deal tonight", "dining"),
        ("Kitchen closing soon", "⏰ Last call orders, 🍔 Quick meal please, 📦 Takeout container ready, 🏃 Rush the order", "dining"),
        ("Waiting list how long?", "⏰ About 20 minutes, 📱 Text when ready, 🍹 Bar seating available, 📅 Reservation next time", "dining"),
        ("Dietary restrictions tonight?", "🥬 Vegetarian options available, 🚫 Gluten free needed, 🥩 Keto friendly options, 🌱 Vegan menu items", "dining"),
        ("Birthday celebration tonight?", "🎂 Birthday dessert special, 🎵 Sing happy birthday, 🎁 Birthday discount available, 📸 Take birthday photo", "dining")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Dining Restaurants",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_travel_vacation():
    """Travel and vacation examples"""
    examples = []
    
    scenarios = [
        ("Planning vacation destination", "🏖️ Beach resort relaxing, 🏔️ Mountain hiking adventure, 🏛️ Historical city tour, 🎢 Theme park fun", "travel"),
        ("Flight booking concerns", "💰 Compare ticket prices, 📅 Flexible travel dates, 🎒 Baggage fees extra, ✈️ Direct flight preferred", "travel"),
        ("Hotel accommodation needs", "🏨 Hotel room booking, 🏠 Vacation rental home, 💰 Budget friendly options, ⭐ Reviews ratings check", "travel"),
        ("Travel insurance worth it?", "💼 Coverage for cancellation, 🏥 Medical emergency coverage, 💰 Cost versus benefits, 📋 Read policy details", "travel"),
        ("Packing for the trip", "🎒 Pack light efficient, ☀️ Weather appropriate clothes, 💊 Medications don't forget, 📱 Phone charger essential", "travel"),
        ("Airport security checkpoint", "📄 Documents ready accessible, 👞 Easy shoes remove, 💻 Electronics bin separate, ⏰ Arrive early enough", "travel"),
        ("Foreign currency exchange", "💱 Exchange rate check, 🏦 Bank currency exchange, 💳 Credit cards accepted, 💰 Cash for tips", "travel"),
        ("Language barrier concerns", "📱 Translation app download, 📚 Basic phrases learn, 🗺️ Point to map, 🤝 Gestures help communicate", "travel"),
        ("Lost luggage situation", "📞 Report to airline, 📋 Fill lost form, 🛒 Essential items buy, ⏰ Check tracking status", "travel"),
        ("Tourist attractions crowded", "⏰ Visit early morning, 📅 Weekday less crowded, 🎫 Skip line tickets, 📸 Quick photo move", "travel"),
        ("Travel jet lag", "😴 Adjust sleep schedule, 💧 Stay hydrated always, ☀️ Natural light exposure, 💊 Melatonin supplement help", "travel"),
        ("Emergency while traveling", "📞 Emergency contact numbers, 🆔 Important documents copies, 💳 Emergency credit card, 🏥 Local hospital location", "travel"),
        ("Cultural etiquette unknown", "📚 Research customs beforehand, 👥 Observe locals behavior, 🤝 When doubt ask, 🙏 Respectful attitude always", "travel"),
        ("Road trip planning", "🗺️ Route planning GPS, ⛽ Gas stations locate, 🏨 Overnight stops plan, 🎵 Music playlist ready", "travel"),
        ("Travel budget exceeded", "💳 Track spending daily, 🍔 Eat local cheaper, 🚶 Walk instead taxi, 🎁 Souvenirs limit spending", "travel")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Travel Vacation",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# I'll continue with the remaining categories using a more efficient approach...

def create_health_fitness():
    """Health and fitness examples"""
    examples = []
    
    scenarios = [
        ("Starting exercise routine", "🏃 Start walking daily, 🏋️ Join gym membership, 👥 Workout buddy find, 📅 Schedule exercise time", "fitness"),
        ("Diet not working", "🍎 Try different approach, 📊 Track food intake, 🩺 Nutritionist consult help, ⏰ Be more patient", "fitness"),
        ("Gym intimidation", "👥 Bring friend along, 🏋️ Personal trainer help, ⏰ Off peak hours, 💪 Start small build", "fitness"),
        ("Weight loss plateau", "🔄 Change workout routine, 🍎 Adjust diet plan, 📊 Track measurements not, ⏰ Plateau is normal", "fitness"),
        ("Exercise motivation lacking", "🎯 Set specific goals, 🎵 Energizing music playlist, 👥 Group fitness classes, 🎁 Reward milestone achievements", "fitness"),
        ("Healthy meal prep", "📅 Plan meals weekly, 🛒 Grocery shopping list, 🍱 Batch cook weekends, 💧 Stay hydrated always", "fitness"),
        ("Sleep quality poor", "📱 Screen time before, 😴 Consistent bedtime routine, 🛏️ Comfortable sleep environment, ☕ Limit caffeine afternoon", "fitness"),
        ("Stress management", "🧘 Meditation practice daily, 🫁 Deep breathing exercises, 🚶 Nature walks calming, 📚 Stress management books", "fitness"),
        ("Workout recovery", "💧 Hydration important always, 🛁 Epsom salt bath, 😴 Adequate sleep needed, 🍎 Protein post workout", "fitness"),
        ("Fitness goal setting", "🎯 Specific measurable goals, 📅 Timeline realistic expectations, 📊 Track progress regularly, 🏆 Celebrate small wins", "fitness"),
        ("Injury prevention", "🏃 Proper warm up, 🧘 Cool down stretching, 👂 Listen to body, 🩺 Form technique correct", "fitness"),
        ("Supplements questions", "🩺 Doctor advice first, 📚 Research evidence based, 💰 Cost benefit analysis, 🍎 Food sources preferred", "fitness")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Health Fitness",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create remaining categories with similar structure...
def create_events_celebrations():
    examples = []
    scenarios = [
        ("Planning birthday party", "🎂 Birthday cake order, 🎈 Decorations party supplies, 👥 Guest list invitations, 🎵 Music playlist create", "events"),
        ("Wedding invitation received", "✉️ RSVP by deadline, 🎁 Gift registry check, 👗 Outfit shopping needed, 📅 Mark calendar date", "events"),
        ("Holiday family gathering", "🍽️ Potluck dish bring, 🏠 Host at house, 🎁 Gifts for everyone, 📞 Coordinate with family", "events"),
        ("Anniversary celebration", "🍾 Special dinner reservations, 💐 Flowers bouquet order, 🎁 Meaningful gift idea, 📸 Photo memories create", "events"),
        ("Graduation ceremony", "🎓 Cap gown rental, 📸 Professional photos book, 🎉 Celebration party plan, 👨‍👩‍👧‍👦 Family tickets needed", "events"),
        ("Baby shower planning", "👶 Theme color scheme, 🎮 Games activities plan, 🍰 Cake dessert order, 📋 Gift registry create", "events"),
        ("Retirement party", "🏆 Career achievements highlight, 🍾 Toast speeches prepare, 📸 Memory photo album, 🎁 Group gift organize", "events"),
        ("New Year's Eve", "🎊 Party plans tonight, 🏠 Quiet celebration home, 📺 Watch ball drop, 🥂 Champagne toast midnight", "events"),
        ("Thanksgiving dinner", "🦃 Turkey cooking prep, 👨‍👩‍👧‍👦 Family traditions continue, 🙏 Gratitude sharing time, 🍰 Pie dessert choices", "events"),
        ("Housewarming party", "🏠 Show new home, 🍕 Casual food serve, 🎁 Housewarming gifts appreciated, 👥 Neighbors invite too", "events"),
        ("School reunion", "👥 Old friends reconnect, 📸 Memory lane photos, 🎵 Music from era, 📅 Save the date", "events"),
        ("Charity fundraiser", "💰 Donation amount decide, 🎫 Event tickets purchase, 👥 Volunteer time offer, 📢 Share with friends", "events")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Events Celebrations",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_banking_finance():
    examples = []
    scenarios = [
        ("Bank account balance low", "💰 Check account balance, 💸 Reduce unnecessary spending, 💼 Look for income, 📞 Call bank overdraft", "banking"),
        ("Credit card debt", "💳 Pay minimum payment, 💰 Debt consolidation consider, 📊 Budget create strict, 💼 Extra income needed", "banking"),
        ("Saving for emergency", "💰 Automatic savings setup, 📊 Budget emergency fund, 🎯 Three months expenses, 🏦 High yield account", "banking"),
        ("Investment planning", "📊 Risk tolerance assess, 💼 Diversify investment portfolio, 📚 Financial advisor consult, ⏰ Long term thinking", "banking"),
        ("Mortgage application", "📋 Financial documents gather, 💰 Down payment save, 📊 Credit score check, 🏠 Pre approval get", "banking"),
        ("Retirement planning", "📊 401k contribution increase, 💰 IRA account open, 📚 Financial planning help, ⏰ Start early important", "banking"),
        ("Insurance claims", "📞 Call insurance company, 📋 Claim forms complete, 📸 Damage photos take, ⏰ Follow up regularly", "banking"),
        ("Tax preparation", "📋 Documents organize early, 💻 Tax software use, 💰 Tax preparer hire, 📅 Deadline approaching fast", "banking"),
        ("Budget not working", "📊 Track spending carefully, 🎯 Realistic budget create, 💸 Cut unnecessary expenses, 📱 Budgeting app use", "banking"),
        ("Financial goals", "🎯 Specific goals write, 📅 Timeline create realistic, 📊 Progress track regularly, 🏆 Celebrate milestone achievements", "banking"),
        ("Identity theft concern", "📞 Credit bureaus call, 💳 Credit report check, 👮 Police report file, 🔒 Accounts freeze immediately", "banking"),
        ("Student loan debt", "💰 Income driven plan, 📋 Loan forgiveness programs, 💸 Extra payments principal, 📞 Loan servicer contact", "banking")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Banking Finance",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create remaining categories efficiently...
def create_neighborhood_community():
    examples = []
    scenarios = [
        ("New neighbor introduction", "👋 Welcome to neighborhood, 🏠 Show around area, 📞 Exchange contact information, 🤝 Offer help settling", "community"),
        ("Neighborhood watch", "👮 Crime prevention important, 👥 Organize watch group, 📞 Emergency contact list, 🏠 Look out neighbors", "community"),
        ("Community event", "🎪 Local festival coming, 👥 Volunteer opportunities available, 🎫 Event tickets purchase, 📅 Mark calendar date", "community"),
        ("Noise complaint", "👂 Talk to neighbor, 📞 Call non emergency, 📝 Document noise times, 🤝 Mediation service help", "community"),
        ("Local government", "🗳️ Vote local elections, 📞 Contact city council, 📋 Attend town meetings, 📢 Voice concerns publicly", "community"),
        ("Block party planning", "🎉 Organize neighborhood party, 🍔 Potluck food organize, 🎵 Music entertainment plan, 📋 Permits needed check", "community"),
        ("Community garden", "🌱 Volunteer garden work, 🥕 Fresh vegetables grow, 👥 Meet gardening neighbors, 🌻 Beautify neighborhood together", "community"),
        ("Local business support", "🛒 Shop local businesses, 📢 Recommend to friends, ⭐ Leave positive reviews, 💰 Support community economy", "community"),
        ("Safety concerns", "👮 Report to police, 💡 Improve street lighting, 👥 Neighbors watch out, 📞 Emergency contact ready", "community"),
        ("HOA issues", "📋 Read HOA rules, 📞 Contact HOA board, 📝 Submit formal complaint, 👥 Attend HOA meetings", "community")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Neighborhood Community",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_pets_animals():
    examples = []
    scenarios = [
        ("Pet health concern", "🐕 Veterinarian appointment schedule, 💊 Medication give correctly, 🩺 Emergency vet clinic, 📋 Symptoms document carefully", "pets"),
        ("New pet adoption", "🏠 Pet proof home, 🛒 Pet supplies buy, 📚 Pet care research, 💰 Budget pet expenses", "pets"),
        ("Pet behavior problems", "🐕 Dog training classes, 📚 Animal behavior books, 🤝 Professional trainer help, ⏰ Consistency patience needed", "pets"),
        ("Pet grooming", "✂️ Professional groomer appointment, 🛁 Bath at home, 🪥 Teeth cleaning important, 💅 Nail trimming needed", "pets"),
        ("Pet travel", "🚗 Pet car carrier, ✈️ Airline pet policies, 🏨 Pet friendly hotels, 📋 Health certificate needed", "pets"),
        ("Pet emergency", "🏥 Emergency vet hospital, 📞 Poison control hotline, 🚗 Transport pet safely, 💳 Emergency fund ready", "pets"),
        ("Pet food", "🍖 High quality food, 💰 Budget friendly options, 🩺 Veterinarian food recommendations, 🥕 Healthy treat alternatives", "pets"),
        ("Pet exercise", "🚶 Daily walks important, 🎾 Play time together, 🏃 Dog park visits, 🧸 Interactive toys provide", "pets"),
        ("Pet socialization", "🐕 Dog park visits, 👥 Pet play dates, 🎓 Puppy socialization classes, 🤝 Gentle exposure new", "pets"),
        ("Pet loss grief", "😢 Grieving process normal, 🤝 Support groups available, 📸 Memory keepsake create, ⏰ Take time heal", "pets")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"My pet needs {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Pets Animals",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_gaming_sports():
    examples = []
    scenarios = [
        ("Gaming session tonight", "🎮 What game play, 👥 Multiplayer online together, 🏆 Tournament mode compete, ⏰ How long play", "gaming"),
        ("Sports team playing", "📺 Watch game tonight, 🏟️ Attend game person, 👥 Sports bar friends, 📊 Check team stats", "gaming"),
        ("New game release", "🛒 Buy game now, ⭐ Check reviews first, 💰 Wait for sale, 📱 Mobile version available", "gaming"),
        ("Fantasy sports league", "📊 Set lineup today, 👥 Trade with others, 🏆 Championship hopes high, 📈 Check player stats", "gaming"),
        ("Recreational sports", "⚽ Join local league, 🏃 Casual pickup games, 🎾 Tennis partner needed, 🏀 Basketball court available", "gaming"),
        ("Gaming equipment", "🎮 New controller needed, 💻 Gaming computer upgrade, 🎧 Good headset important, 🪑 Gaming chair comfort", "gaming"),
        ("Sports betting", "💰 Bet responsibly limits, 📊 Research teams first, 🎯 Fun entertainment only, 🚫 Don't chase losses", "gaming"),
        ("Board game night", "🎲 What games play, 👥 How many players, 🍕 Snacks for night, 🏠 Host at house", "gaming"),
        ("Fitness gaming", "🕺 Dance video games, 🏃 Running game apps, 🥊 Boxing workout games, 📊 Track fitness progress", "gaming"),
        ("Competitive gaming", "🏆 Esports tournament join, 💪 Practice skills daily, 👥 Team formation needed, 📊 Ranking climb goals", "gaming")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Gaming Sports",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_diy_crafts():
    examples = []
    scenarios = [
        ("DIY project ideas", "🔨 Woodworking project start, 🎨 Painting room walls, 🧵 Sewing craft project, 🌱 Garden project create", "diy"),
        ("Craft supplies needed", "🛒 Craft store shopping, 💰 Budget supplies cost, 📦 Online ordering delivery, ♻️ Repurpose materials home", "diy"),
        ("Tool borrowing", "🔧 Borrow from neighbor, 🏪 Rent tools store, 💰 Buy tools invest, 🤝 Ask family help", "diy"),
        ("Project not working", "📚 Check tutorial again, 🤝 Ask expert help, 🔄 Try different approach, ⏰ Take break return", "diy"),
        ("Home improvement project", "🏠 Kitchen renovation plan, 🛁 Bathroom update ideas, 🎨 Paint interior walls, 🔧 Fix broken things", "diy"),
        ("Craft gift making", "🎁 Handmade gifts special, ⏰ Start early enough, 📚 Find tutorial online, 🎨 Personal touch add", "diy"),
        ("Workshop space", "🏠 Garage workspace setup, 🔧 Organize tools properly, 💡 Good lighting important, 🧹 Keep area clean", "diy"),
        ("Safety precautions", "🥽 Safety glasses wear, 🧤 Gloves protect hands, 📚 Read instructions first, 🚨 First aid ready", "diy")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC DIY Crafts",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_news_current_events():
    examples = []
    scenarios = [
        ("Current events discussion", "📰 Read news daily, 📺 Watch news programs, 📱 Social media updates, 🤔 Multiple sources check", "news"),
        ("Political opinions", "🗳️ Voting is important, 💬 Respectful dialogue always, 📚 Research issues thoroughly, 👂 Listen different views", "news"),
        ("World events concerning", "🌍 Global issues complex, 🤝 How can help, 💰 Donate to causes, 📢 Raise awareness share", "news"),
        ("Local news important", "🏛️ City council meetings, 📰 Local newspaper read, 👥 Community issues affect, 🗳️ Local elections matter", "news"),
        ("Breaking news alert", "📱 Check reliable sources, 🤔 Verify information accuracy, 📢 Share responsibly others, ⏰ Developing story wait", "news"),
        ("Media bias concerns", "📚 Multiple news sources, 🤔 Critical thinking apply, 📊 Fact checking important, 💬 Discuss with others", "news"),
        ("Social issues", "🤝 How can help, 💰 Support relevant causes, 📢 Raise awareness share, 🗳️ Vote for change", "news"),
        ("Economic news", "💰 Personal finance impact, 📊 Market trends understand, 💼 Job market effects, 📈 Long term planning", "news")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want to {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC News Current Events",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_future_planning():
    examples = []
    scenarios = [
        ("Retirement dreams", "🏖️ Beach house someday, 🚐 RV travel country, 👨‍👩‍👧‍👦 Time with family, 🎨 Pursue creative hobbies", "future"),
        ("Legacy planning", "📚 Write family history, 🎓 Education fund children, 💰 Estate planning important, 📸 Memory preservation project", "future"),
        ("Long term goals", "🏠 Dream home someday, 💼 Career advancement plans, 🌍 Travel world extensively, 📚 Learn new skills", "future"),
        ("Family planning", "👶 Children in future, 👨‍👩‍👧‍👦 Family size decisions, 🏠 Bigger home needed, 💰 Financial planning children", "future"),
        ("Technology changes", "🤖 AI technology impact, 💻 Digital world evolution, 📚 Continuous learning important, 🔄 Adapt to changes", "future"),
        ("Health aging", "🏋️ Stay active healthy, 🩺 Preventive healthcare important, 🧠 Mental health maintain, 💰 Healthcare costs plan", "future"),
        ("Environmental future", "🌱 Sustainable living choices, ♻️ Reduce environmental impact, 🌍 Climate change prepare, 💚 Green technology adopt", "future"),
        ("Generational wealth", "💰 Financial legacy build, 📚 Education investment priority, 🏠 Property investment consider, 💼 Business ownership goals", "future")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I dream of {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Future Planning",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def parse_output_to_tiles(output_text):
    """Parse output into tile format"""
    tiles = []
    parts = output_text.split(', ')
    
    for i, part in enumerate(parts[:4]):  # Max 4 tiles
        part = part.strip()
        if not part:
            continue
            
        # Find emoji and words
        emoji = ""
        words = part
        
        # Extract emoji if present
        for char in part:
            if ord(char) > 127:  # Non-ASCII character (likely emoji)
                emoji = char
                words = part.replace(char, '').strip()
                break
        
        if not emoji:
            emoji = "💬"  # Default emoji
        
        tiles.append({
            "emoji": emoji,
            "words": words,
            "tile_id": f"tile_{i+1}"
        })
    
    return tiles

if __name__ == "__main__":
    total = create_missing_categories()
    print(f"\n🎯 COMPREHENSIVE CATEGORIES: {total:,} new examples created!")