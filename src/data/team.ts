export interface TeamMember {
  name: string;
  slug: string;
  title: string;
  bio: string;
  image?: string; // Optional path to headshot image
  pronouns?: string; // Pronouns (e.g., "she/her", "they/them")
  specialties?: string[]; // Areas of specialty
  insurancePlans?: string[]; // Insurance plans accepted
  fullBio?: string; // Full detailed bio content
  specialSections?: { title: string; content: string }[]; // Special sections like "WOMEN'S ISSUES", "MIND AND BODY"
  foundedYear?: number; // Year the practice was founded (for founders)
}

export const teamMembers: TeamMember[] = [
  {
    name: "Dr. Lacey Wright",
    slug: "dr-lacey-wright",
    title: "Licensed Clinical Psychologist",
    bio: "Licensed clinical psychologist since 2012; PsyD 2011; specialties include trauma, depression, anxiety, women's issues; uses CBT/ACT/MI; offers walk-and-talk therapy.",
    image: "/team/lacey-wright.jpg",
    pronouns: "she/her",
    specialties: [
      "Trauma/complex trauma",
      "Depression",
      "Mood Disorders",
      "Anxiety",
      "Women's Issues",
      "Adjustment/Grief",
      "Mindfulness",
      "Relationships",
      "Cognitive Decline/Dementia",
      "Assessment/Testing"
    ],
    insurancePlans: [
      "Aetna",
      "Blue Cross Blue Shield",
      "Cigna/Evernorth",
      "Medicare Part B",
      "Magellan",
      "Optum/UHC"
    ],
    foundedYear: 2014,
    fullBio: `I have been a licensed clinical psychologist in the state of Texas since 2012, and completed my Doctor of Psychology (PsyD) degree in 2011 from Midwestern University in Downers Grove, Illinois. I have worked with a variety of populations in many settings, including several psychiatric hospitals, an outpatient addiction center, a county mental health center, a juvenile department and runaway shelter, as a rehabilitation psychologist for a largely geriatric population, and now in full time private practice. I have specifically targeted my training experiences to provide me a well-rounded set of therapeutic skills to address many life issues.

My theoretical orientation, or the way I approach psychotherapy with my patients, is a combination of several evidence-based treatments, primarily Cognitive-Behavioral Therapy (CBT), Acceptance and Commitment Therapy (ACT), Motivational Interviewing (MI) and trauma-informed approaches. With these approaches, we will explore thoughts, feelings, and behaviors/reactions, and how they might limit you in the present, as well as build upon your individual strengths. I believe each person is different, and my focus is on your symptoms and goals, rather than a diagnostic label. I will work with you to best address your needs and overall wellness. I value innovation, learning, and growth, and am always working to provide the most current treatment services available.

I founded Wright Wellness to create a compassionate and supportive environment for both our patients and our clinical team. My ultimate goal is to provide quality and accessible mental health services in the private practice setting, and work towards reducing the stigma of mental health treatment one session at a time.`,
    specialSections: [
      {
        title: "WOMEN'S ISSUES",
        content: "The majority of my clinical research has focused primarily on women's issues, including the individual needs of women and their ideal treatment outcomes. Because of my time devoted to this topic, I have a continued special interest in working with women. If you are a woman needing extra support and guidance during a difficult life transition or issue, contact me and we can further explore your goals."
      },
      {
        title: "MIND AND BODY",
        content: "I also have a special interest in the relationship between the mind and the body, and I believe overall wellness comes from both mental and physical health. Therefore, I also highly encourage the consideration of walk and talk therapy, a newer therapeutic approaches that involves walking during psychotherapy sessions, which incorporates the whole body. If you are interested in this service, let me know, I would be happy to discuss it with you further."
      }
    ]
  },
  {
    name: "Dr. Dana Shafir",
    slug: "dr-dana-shafir-lpc",
    title: "LPC, CHC",
    bio: "Doctoral-level LPC (TWU, 2005). Experience in varied settings; offers health coaching; focus on lifestyle and integrative approaches."
  },
  {
    name: "Dr. Laura Ávila",
    slug: "dr-laura-avila",
    title: "Licensed Psychologist",
    bio: "Specialized training in CPT and Prolonged Exposure for PTSD; integrated care experience; master's in psychopharmacology."
  },
  {
    name: "Alexandra (Allie) Glenn",
    slug: "alexandra-glenn",
    title: "LPC",
    bio: "Eclectic CBT/DBT skills-based approach; telehealth-only."
  },
  {
    name: "Anna (Mea) McMahon",
    slug: "anna-mea-mcmahon-lpc",
    title: "LPC",
    bio: "LPC since 2013 with diverse settings (private practice, hospitals, group homes, rehab, community MH)."
  },
  {
    name: "Brittanie Okon",
    slug: "brittanie-okon",
    title: "Office Manager & Coordinator",
    bio: "Admin support so clients can focus on care; with WW since 2018."
  },
  {
    name: "Elisabeth Davenport",
    slug: "elisabeth-davenport-lpc-associate-1",
    title: "LPC Associate, CRC",
    bio: "UNT-trained; CRC; humanistic approaches; supervised by Ashley Hendricks, LPC-S."
  },
  {
    name: "Ernest Smith",
    slug: "ernest-smith-lpc",
    title: "LPC",
    bio: "Supports adolescents, young adults, elderly through grief/anxiety/depression; safe, professional, compassionate."
  },
  {
    name: "Janelle Linares",
    slug: "janelle-linares",
    title: "LPC",
    bio: "Bilingual LPC (EN/ES); trauma-informed since 2014 across courts, hospitals, shelters; telehealth-only; Spanish available."
  },
  {
    name: "Jessica Kolar",
    slug: "jessica-kolar-lpc",
    title: "LPC",
    bio: "Works with children, adolescents, and adults; passionate about adolescent transitions; treats anxiety, depression, trauma, attachment, parenting."
  },
  {
    name: "Karalee Landers-Oliveira",
    slug: "karalee-landers-aprn",
    title: "PMHNP",
    bio: "PMHNP providing med management for 13+; specialties include depression, anxiety, ADHD, sleep and mood disorders."
  },
  {
    name: "Lyndsey Martin",
    slug: "lyndsey-martin",
    title: "LPC",
    bio: "Specialties: depression, anxiety, trauma, eating disorders, young adults; uses DBT/ACT/EMDR; telehealth-only."
  },
  {
    name: "Ruth Bucher",
    slug: "ruth-bucher",
    title: "LMT",
    bio: "Advanced bodywork modalities; specialties include pain, trauma recovery, neurological conditions; customized sessions."
  },
  {
    name: "Shelby Upton",
    slug: "shelby-upton-lpc-associate",
    title: "LPC Associate",
    bio: "LPC Associate since 2019; experience across private practices; supervised."
  },
  {
    name: "Shirley Bravo",
    slug: "shirley-bravo",
    title: "LMFT Associate",
    bio: "Bilingual LMFT Associate; EMDR/CBT; couples/families/veterans/first responders; supervised."
  },
  {
    name: "Trish Garner",
    slug: "trish-garner-billing-manager",
    title: "Billing Manager",
    bio: "Healthcare admin since 2014; billing specialization; compassionate, efficient support."
  },
];

