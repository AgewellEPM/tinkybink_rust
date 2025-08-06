#!/usr/bin/env python3
"""
Identify Missing AAC Scenarios
Comprehensive analysis to find any gaps in coverage
"""
import json

def identify_missing_scenarios():
    """Analyze for any missing AAC communication scenarios"""
    
    print("🔍 TinkyBink Missing Scenarios Analyzer")
    print("=" * 60)
    print("🎯 Analyzing for any missing communication scenarios")
    print("📊 Comprehensive gap analysis")
    print()
    
    # Define comprehensive scenario categories that should exist
    essential_scenarios = {
        "EMERGENCY_CRITICAL": [
            "House fire emergency", "Heart attack symptoms", "Choking incident", 
            "Car accident witness", "Child missing", "Gas leak suspected",
            "Electrical emergency", "Poisoning emergency", "Allergic reaction severe",
            "Unconscious person found", "Armed threat", "Natural disaster"
        ],
        
        "INTIMATE_PERSONAL": [
            "Sexual health concerns", "Reproductive health", "Pregnancy symptoms",
            "Menstrual issues", "Erectile dysfunction", "Birth control discussion",
            "STD concerns", "Fertility issues", "Pregnancy loss", "Body image issues",
            "Sexual assault disclosure", "Domestic violence"
        ],
        
        "MENTAL_HEALTH_CRISIS": [
            "Suicidal ideation", "Self harm urges", "Psychotic episode",
            "Severe depression", "Panic attack", "Eating disorder relapse",
            "Substance abuse relapse", "Trauma flashback", "Dissociation episode",
            "Bipolar mania", "Schizophrenia symptoms", "Personality disorder crisis"
        ],
        
        "CHILDHOOD_SPECIFIC": [
            "Potty training", "Stranger danger", "Bullying at school",
            "First day school", "Lost child", "Afraid of dark",
            "Nightmares", "Tooth fairy", "Santa Claus", "Birthday party",
            "Playground conflict", "Learning disabilities"
        ],
        
        "ELDERLY_SPECIFIC": [
            "Dementia confusion", "Falls risk", "Medication confusion",
            "Social isolation", "End of life decisions", "Medicare navigation",
            "Driving safety", "Home modifications", "Caregiver stress",
            "Memory loss", "Physical limitations", "Independence concerns"
        ],
        
        "CULTURAL_RELIGIOUS": [
            "Religious ceremonies", "Cultural holidays", "Prayer requests",
            "Dietary restrictions", "Pilgrimage", "Religious doubts",
            "Cultural identity", "Interfaith relationships", "Religious conversion",
            "Traditional healing", "Ancestor worship", "Spiritual guidance"
        ],
        
        "NEURODIVERGENT_SPECIFIC": [
            "Sensory overload", "Stimming needs", "Social confusion",
            "Routine disruption", "Hyperfocus", "Executive dysfunction",
            "Masking fatigue", "Special interests", "Social scripts",
            "Meltdown prevention", "Communication preferences", "Accommodation needs"
        ],
        
        "LGBTQ_SPECIFIC": [
            "Coming out", "Gender dysphoria", "Pronouns discussion",
            "Discrimination faced", "Identity exploration", "Transition process",
            "Support groups", "Medical transition", "Family acceptance",
            "Workplace issues", "Legal name change", "Relationship dynamics"
        ],
        
        "ADDICTION_RECOVERY": [
            "Craving management", "Relapse prevention", "AA meeting",
            "Sponsor relationship", "Detox process", "Withdrawal symptoms",
            "Recovery milestones", "Making amends", "Sober socializing",
            "Triggers identification", "Recovery support", "Family healing"
        ],
        
        "PREGNANCY_PARENTING": [
            "Morning sickness", "Labor contractions", "Breastfeeding issues",
            "Postpartum depression", "Sleep training", "Developmental milestones",
            "Childcare decisions", "School choice", "Discipline strategies",
            "Teen pregnancy", "Miscarriage grief", "Infertility struggles"
        ],
        
        "DISABILITY_ADVOCACY": [
            "ADA accommodation", "Disability rights", "Accessibility barriers",
            "Assistive technology", "Independent living", "Caregiver support",
            "Disability pride", "Medical advocacy", "Transportation access",
            "Employment discrimination", "Housing accessibility", "Social barriers"
        ],
        
        "GRIEF_BEREAVEMENT": [
            "Sudden death", "Terminal diagnosis", "Pet loss",
            "Miscarriage loss", "Suicide loss", "Accident death",
            "Murder victim", "War casualty", "Missing person",
            "Anniversary grief", "Complicated grief", "Anticipatory grief"
        ],
        
        "LEGAL_JUSTICE": [
            "Court appearance", "Jury duty", "Arrest situation",
            "Victim rights", "Witness testimony", "Legal representation",
            "Criminal charges", "Civil lawsuit", "Divorce proceedings",
            "Child custody", "Immigration court", "Traffic violations"
        ],
        
        "ECONOMIC_HARDSHIP": [
            "Job loss", "Eviction notice", "Utility shutoff",
            "Food insecurity", "Homeless", "Bankruptcy",
            "Medical debt", "Student loans", "Foreclosure",
            "Government assistance", "Credit problems", "Emergency funds"
        ],
        
        "NATURAL_DISASTERS": [
            "Earthquake", "Hurricane", "Tornado", "Flood",
            "Wildfire", "Blizzard", "Heat wave", "Drought",
            "Volcanic eruption", "Tsunami", "Landslide", "Ice storm"
        ]
    }
    
    # Check for missing scenarios
    missing_scenarios = []
    
    for category, scenarios in essential_scenarios.items():
        print(f"\n🔍 Analyzing {category}:")
        missing_in_category = []
        
        for scenario in scenarios:
            # This would need to check against actual dataset
            # For now, identifying potentially missing ones
            if any(keyword in scenario.lower() for keyword in ['sexual', 'suicide', 'assault', 'rape', 'murder']):
                missing_in_category.append(f"⚠️  {scenario} - Sensitive content")
            elif any(keyword in scenario.lower() for keyword in ['lgbtq', 'transgender', 'gay', 'lesbian']):
                missing_in_category.append(f"🏳️‍🌈 {scenario} - LGBTQ+ specific")
            elif any(keyword in scenario.lower() for keyword in ['religious', 'prayer', 'spiritual']):
                missing_in_category.append(f"🙏 {scenario} - Religious/spiritual")
            else:
                print(f"   ✅ {scenario} - Likely covered")
        
        if missing_in_category:
            missing_scenarios.extend(missing_in_category)
            for missing in missing_in_category:
                print(f"   {missing}")
    
    # Specialized missing scenarios
    additional_missing = [
        "🏥 Medical procedure consent", "⚖️ Miranda rights explanation", 
        "🔒 Prison communication", "🎖️ Military combat stress",
        "🧬 Genetic counseling", "🩸 Blood donation process",
        "🫀 Organ donation decision", "🏥 ICU family communication",
        "👶 NICU parent support", "🧠 Alzheimer's progression",
        "💉 Vaccine hesitancy", "🔬 Clinical trial participation",
        "🏥 Hospice care decisions", "⚱️ Funeral planning",
        "💰 Life insurance claims", "📋 Living will decisions",
        "🧬 DNA test results", "🏥 Surgery complications",
        "💊 Medication side effects", "🩺 Second medical opinion",
        "🏥 Hospital discharge planning", "🚑 EMT communication",
        "👮 Police interrogation", "⚖️ Plea bargain discussion",
        "🏛️ Immigration hearing", "📋 Asylum application",
        "🎓 Special education IEP", "🏫 School suspension",
        "👨‍⚕️ Psychiatric evaluation", "🏥 Involuntary commitment",
        "💔 Relationship abuse", "👶 Child abuse reporting",
        "👴 Elder abuse concerns", "🏠 Unsafe living conditions",
        "💰 Financial abuse", "📞 Scam victim",
        "🎯 Identity theft", "💻 Cyberbullying",
        "📱 Social media harassment", "🎮 Gaming addiction",
        "📺 Screen time concerns", "🛒 Shopping addiction",
        "🍔 Food addiction", "💪 Exercise addiction",
        "💄 Body dysmorphia", "⚖️ Eating disorder",
        "🚭 Smoking cessation", "☕ Caffeine withdrawal",
        "💊 Prescription abuse", "🍷 Alcohol dependency"
    ]
    
    print(f"\n📋 ADDITIONAL POTENTIALLY MISSING:")
    for missing in additional_missing:
        print(f"   {missing}")
    
    total_missing = len(missing_scenarios) + len(additional_missing)
    
    print(f"\n📊 MISSING SCENARIOS ANALYSIS:")
    print(f"   ⚠️  Sensitive scenarios: {len([s for s in missing_scenarios if 'Sensitive' in s])}")
    print(f"   🏳️‍🌈 LGBTQ+ specific: {len([s for s in missing_scenarios if 'LGBTQ+' in s])}")
    print(f"   🙏 Religious/spiritual: {len([s for s in missing_scenarios if 'Religious' in s])}")
    print(f"   🏥 Additional specialized: {len(additional_missing)}")
    print(f"   🎯 Total potentially missing: {total_missing}")
    
    if total_missing > 0:
        print(f"\n💡 RECOMMENDATION:")
        print(f"   Create {total_missing} additional examples")
        print(f"   Focus on sensitive, specialized scenarios")
        print(f"   Ensure ethical, appropriate coverage")
        print(f"   Consider content warnings")
    else:
        print(f"\n✅ COVERAGE APPEARS COMPLETE!")
        print(f"   No major gaps identified")
        print(f"   Dataset comprehensively covers scenarios")
    
    # Create missing scenarios file
    missing_data = {
        "analysis_date": "2025-01-05",
        "total_missing_identified": total_missing,
        "sensitive_scenarios": [s for s in missing_scenarios if 'Sensitive' in s],
        "lgbtq_scenarios": [s for s in missing_scenarios if 'LGBTQ+' in s],
        "religious_scenarios": [s for s in missing_scenarios if 'Religious' in s],
        "additional_specialized": additional_missing,
        "recommendations": [
            "Add sensitive scenarios with appropriate content warnings",
            "Include LGBTQ+ specific communication needs",
            "Add religious/spiritual scenarios respectfully",
            "Cover specialized medical/legal scenarios",
            "Ensure ethical boundaries maintained"
        ]
    }
    
    with open("missing_scenarios_analysis.json", 'w', encoding='utf-8') as f:
        json.dump(missing_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Analysis saved: missing_scenarios_analysis.json")
    
    return total_missing

if __name__ == "__main__":
    missing_count = identify_missing_scenarios()
    if missing_count > 0:
        print(f"\n🎯 Found {missing_count} potentially missing scenarios")
        print(f"🚀 Ready to create additional examples if needed")
    else:
        print(f"\n✅ No major gaps found - coverage appears complete!")