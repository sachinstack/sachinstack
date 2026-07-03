import React, { useState } from 'react';
import { Activity, Utensils, TrendingUp, Heart, Zap, Target, Menu, X, Award, Clock, Flame, Dumbbell } from 'lucide-react';

export default function CompleteFitnessWebsite() {
  const [activeTab, setActiveTab] = useState('home');
  const [selectedWorkout, setSelectedWorkout] = useState(null);
  const [weight, setWeight] = useState('');
  const [progressData, setProgressData] = useState([]);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [userName, setUserName] = useState('');
  const [userGoal, setUserGoal] = useState('muscle');

  // ==================== ALL WORKOUTS ====================
  const workouts = [
    {
      id: 1,
      name: 'Chest & Triceps',
      duration: '45 mins',
      difficulty: 'Intermediate',
      calories: 350,
      level: 'Level 3',
      exercises: [
        { name: 'Push-ups', sets: 3, reps: 15, rest: '60 sec' },
        { name: 'Bench Press', sets: 4, reps: 8, rest: '90 sec' },
        { name: 'Tricep Dips', sets: 3, reps: 12, rest: '60 sec' },
        { name: 'Cable Flyes', sets: 3, reps: 12, rest: '45 sec' },
        { name: 'Tricep Rope Pushdown', sets: 3, reps: 15, rest: '45 sec' }
      ]
    },
    {
      id: 2,
      name: 'Back & Biceps',
      duration: '50 mins',
      difficulty: 'Intermediate',
      calories: 380,
      level: 'Level 3',
      exercises: [
        { name: 'Pull-ups', sets: 4, reps: 10, rest: '90 sec' },
        { name: 'Barbell Rows', sets: 4, reps: 8, rest: '90 sec' },
        { name: 'Bicep Curls', sets: 3, reps: 12, rest: '60 sec' },
        { name: 'Lat Pulldowns', sets: 3, reps: 12, rest: '60 sec' },
        { name: 'Face Pulls', sets: 3, reps: 15, rest: '45 sec' }
      ]
    },
    {
      id: 3,
      name: 'Legs & Glutes',
      duration: '55 mins',
      difficulty: 'Hard',
      calories: 450,
      level: 'Level 4',
      exercises: [
        { name: 'Squats', sets: 4, reps: 10, rest: '90 sec' },
        { name: 'Deadlifts', sets: 3, reps: 6, rest: '120 sec' },
        { name: 'Leg Press', sets: 3, reps: 12, rest: '90 sec' },
        { name: 'Leg Curls', sets: 3, reps: 12, rest: '60 sec' },
        { name: 'Calf Raises', sets: 4, reps: 15, rest: '45 sec' }
      ]
    },
    {
      id: 4,
      name: 'Cardio Blast',
      duration: '30 mins',
      difficulty: 'Beginner',
      calories: 300,
      level: 'Level 2',
      exercises: [
        { name: 'Warm-up Running', duration: '5 mins', intensity: 'Easy' },
        { name: 'High Intensity Sprints', duration: '15 mins', intensity: 'Hard' },
        { name: 'Cool-down Walk', duration: '10 mins', intensity: 'Easy' }
      ]
    },
    {
      id: 5,
      name: 'Shoulders & Arms',
      duration: '40 mins',
      difficulty: 'Intermediate',
      calories: 320,
      level: 'Level 3',
      exercises: [
        { name: 'Military Press', sets: 4, reps: 8, rest: '90 sec' },
        { name: 'Lateral Raises', sets: 3, reps: 12, rest: '60 sec' },
        { name: 'Overhead Press', sets: 3, reps: 10, rest: '75 sec' },
        { name: 'Hammer Curls', sets: 3, reps: 12, rest: '60 sec' }
      ]
    },
    {
      id: 6,
      name: 'Core & Abs',
      duration: '25 mins',
      difficulty: 'Beginner',
      calories: 150,
      level: 'Level 1',
      exercises: [
        { name: 'Planks', sets: 3, duration: '30 sec', rest: '30 sec' },
        { name: 'Crunches', sets: 3, reps: 20, rest: '45 sec' },
        { name: 'Russian Twists', sets: 3, reps: 20, rest: '45 sec' },
        { name: 'Leg Raises', sets: 3, reps: 12, rest: '60 sec' }
      ]
    },
    {
      id: 7,
      name: 'Full Body Strength',
      duration: '60 mins',
      difficulty: 'Hard',
      calories: 500,
      level: 'Level 4',
      exercises: [
        { name: 'Barbell Squats', sets: 4, reps: 8, rest: '120 sec' },
        { name: 'Bench Press', sets: 3, reps: 8, rest: '120 sec' },
        { name: 'Barbell Rows', sets: 3, reps: 8, rest: '120 sec' },
        { name: 'Deadlifts', sets: 2, reps: 5, rest: '150 sec' }
      ]
    },
    {
      id: 8,
      name: 'Flexibility & Stretching',
      duration: '20 mins',
      difficulty: 'Beginner',
      calories: 50,
      level: 'Level 1',
      exercises: [
        { name: 'Full Body Stretch', duration: '5 mins' },
        { name: 'Yoga Flow', duration: '10 mins' },
        { name: 'Cool Down Breathing', duration: '5 mins' }
      ]
    }
  ];

  // ==================== ALL NUTRITION PLANS ====================
  const nutritionPlans = [
    {
      title: 'Protein Intake',
      description: 'खाने में प्रोटीन जरूर शामिल करें - 0.8-1g प्रोटीन प्रति lb body weight',
      icon: '🍗',
      tips: ['Chicken', 'Fish', 'Eggs', 'Milk', 'Almonds']
    },
    {
      title: 'Hydration (पानी)',
      description: 'रोज 3-4 लीटर पानी पिएं - अच्छे परफॉर्मेंस के लिए बहुत जरूरी',
      icon: '💧',
      tips: ['सुबह खाली पेट 1 गिलास', 'व्यायाम से पहले 500ml', 'व्यायाम के दौरान हर 15 मिनट में', 'रात को सोने से 1 घंटा पहले']
    },
    {
      title: 'Complex Carbs',
      description: 'अच्छी energy के लिए brown rice, oats, और sweet potatoes खाएं',
      icon: '🌾',
      tips: ['Brown Rice', 'Oats', 'Whole Wheat Bread', 'Sweet Potatoes', 'Quinoa']
    },
    {
      title: 'Healthy Fats',
      description: 'Hormonal health के लिए healthy fats बहुत जरूरी हैं',
      icon: '🥑',
      tips: ['Almonds', 'Avocados', 'Olive Oil', 'Coconut Oil', 'Peanut Butter']
    },
    {
      title: 'Fruits & Vegetables',
      description: 'अलग-अलग रंग के फल और सब्जियां खाएं vitamins के लिए',
      icon: '🥕',
      tips: ['Green Vegetables', 'Bananas', 'Berries', 'Oranges', 'Spinach']
    },
    {
      title: 'Meal Timing',
      description: 'सही समय पर खाना खाना शरीर के लिए बहुत फायदेमंद है',
      icon: '⏰',
      tips: ['Breakfast: 6-8 AM', 'Mid-Morning: 10 AM', 'Lunch: 1-2 PM', 'Evening Snack: 4-5 PM', 'Dinner: 7-8 PM']
    }
  ];

  // ==================== ADD WEIGHT TO PROGRESS ====================
  const handleAddProgress = () => {
    if (weight) {
      const newEntry = {
        date: new Date().toLocaleDateString('en-IN'),
        weight: parseFloat(weight),
        time: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })
      };
      setProgressData([...progressData, newEntry]);
      setWeight('');
    }
  };

  // ==================== DELETE PROGRESS ====================
  const handleDeleteProgress = (index) => {
    setProgressData(progressData.filter((_, i) => i !== index));
  };

  // ==================== CALCULATE STATS ====================
  const getProgressStats = () => {
    if (progressData.length === 0) return null;
    const weights = progressData.map(d => d.weight);
    const current = weights[weights.length - 1];
    const initial = weights[0];
    const change = (current - initial).toFixed(1);
    const max = Math.max(...weights);
    const min = Math.min(...weights);
    return { current, initial, change, max, min };
  };

  const stats = getProgressStats();

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-black text-white">
      {/* ==================== NAVIGATION ==================== */}
      <nav className="bg-black/50 backdrop-blur-md sticky top-0 z-50 border-b border-blue-500/20">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center gap-3">
              <Zap className="text-yellow-400" size={32} />
              <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                💪 FitPro
              </h1>
            </div>

            {/* Desktop Menu */}
            <div className="hidden md:flex gap-4">
              {['home', 'workouts', 'nutrition', 'progress'].map(tab => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`px-4 py-2 rounded-lg transition-all font-semibold ${
                    activeTab === tab
                      ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/50'
                      : 'text-gray-300 hover:text-white hover:bg-blue-500/20'
                  }`}
                >
                  {tab.charAt(0).toUpperCase() + tab.slice(1)}
                </button>
              ))}
            </div>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden"
            >
              {mobileMenuOpen ? <X size={28} /> : <Menu size={28} />}
            </button>
          </div>

          {/* Mobile Menu */}
          {mobileMenuOpen && (
            <div className="md:hidden mt-4 flex flex-col gap-2">
              {['home', 'workouts', 'nutrition', 'progress'].map(tab => (
                <button
                  key={tab}
                  onClick={() => {
                    setActiveTab(tab);
                    setMobileMenuOpen(false);
                  }}
                  className={`px-4 py-2 rounded-lg transition-all text-left ${
                    activeTab === tab
                      ? 'bg-blue-500 text-white'
                      : 'text-gray-300 hover:bg-blue-500/20'
                  }`}
                >
                  {tab.charAt(0).toUpperCase() + tab.slice(1)}
                </button>
              ))}
            </div>
          )}
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* ==================== HOME TAB ==================== */}
        {activeTab === 'home' && (
          <div className="space-y-8">
            {/* Welcome Section */}
            <div className="text-center space-y-4">
              <h2 className="text-5xl md:text-6xl font-bold mb-4 bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                आपका Fitness Journey शुरु करें 🚀
              </h2>
              <p className="text-xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
                स्वस्थ जीवन के लिए सही workout, proper nutrition, और dedication की जरूरत है।
                आज ही अपने सपनों का शरीर बनाना शुरु करें!
              </p>
            </div>

            {/* User Goal Selection */}
            <div className="bg-gradient-to-r from-blue-600/20 to-purple-600/20 border border-blue-500/30 rounded-2xl p-8">
              <h3 className="text-2xl font-bold mb-6">👤 अपना Goal चुनें</h3>
              <div className="grid md:grid-cols-3 gap-4 mb-6">
                {[
                  { id: 'muscle', label: '💪 Muscle Gain', color: 'from-red-500' },
                  { id: 'weight', label: '⚖️ Weight Loss', color: 'from-blue-500' },
                  { id: 'strength', label: '🏋️ Strength', color: 'from-orange-500' }
                ].map(goal => (
                  <button
                    key={goal.id}
                    onClick={() => setUserGoal(goal.id)}
                    className={`p-4 rounded-xl font-semibold transition-all ${
                      userGoal === goal.id
                        ? `bg-gradient-to-r ${goal.color} to-transparent text-white border-2 border-white`
                        : 'bg-gray-700/30 border border-gray-600 hover:border-gray-400'
                    }`}
                  >
                    {goal.label}
                  </button>
                ))}
              </div>
              <input
                type="text"
                placeholder="अपना नाम बताएं (Optional)"
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
                className="w-full bg-black/30 border border-blue-500/20 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50"
              />
            </div>

            {/* Features Grid */}
            <div className="grid md:grid-cols-3 gap-6">
              {[
                { icon: Heart, title: '❤️ Cardio', desc: 'दिल को स्वस्थ रखें और stamina बढ़ाएं' },
                { icon: Dumbbell, title: '💪 Strength', desc: 'मांसपेशी बढ़ाएं और ताकत लगाएं' },
                { icon: TrendingUp, title: '📈 Progress', desc: 'अपनी प्रगति ट्रैक करें और motivated रहें' }
              ].map((item, i) => (
                <div
                  key={i}
                  className="bg-gradient-to-br from-blue-500/10 to-purple-500/10 border border-blue-500/30 rounded-2xl p-8 hover:border-blue-500/60 hover:shadow-lg hover:shadow-blue-500/20 transition-all duration-300 cursor-pointer transform hover:scale-105"
                >
                  <item.icon size={48} className="text-blue-400 mb-4" />
                  <h3 className="text-2xl font-bold mb-3">{item.title}</h3>
                  <p className="text-gray-300 leading-relaxed">{item.desc}</p>
                </div>
              ))}
            </div>

            {/* CTA Button */}
            <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-12 text-center relative overflow-hidden">
              <div className="absolute inset-0 opacity-30 bg-[radial-gradient(circle_at_center,transparent_0%,black_100%)]"></div>
              <div className="relative z-10">
                <h3 className="text-4xl font-bold mb-4">आज ही शुरु करें! 🎯</h3>
                <p className="text-lg mb-8 text-gray-100 max-w-2xl mx-auto">
                  अपने फिटनेस लक्ष्य को पूरा करने के लिए सही workout plan चुनें।
                  कोई भी देर नहीं - अभी ही शुरु करो!
                </p>
                <button
                  onClick={() => setActiveTab('workouts')}
                  className="bg-white text-blue-600 font-bold px-10 py-4 rounded-xl hover:bg-gray-100 transition-all text-lg shadow-lg hover:shadow-2xl hover:scale-105 transform"
                >
                  Workouts देखें →
                </button>
              </div>
            </div>
          </div>
        )}

        {/* ==================== WORKOUTS TAB ==================== */}
        {activeTab === 'workouts' && (
          <div className="space-y-8">
            <div>
              <h2 className="text-5xl font-bold mb-3">💪 Workout Plans</h2>
              <p className="text-gray-400">अपने लिए सही workout चुनें और शुरु करें</p>
            </div>

            {!selectedWorkout ? (
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {workouts.map(workout => (
                  <div
                    key={workout.id}
                    onClick={() => setSelectedWorkout(workout)}
                    className="bg-gradient-to-br from-blue-500/10 to-purple-500/10 border border-blue-500/30 rounded-2xl p-6 hover:border-blue-500/60 hover:shadow-lg hover:shadow-blue-500/20 transition-all cursor-pointer transform hover:scale-105 group"
                  >
                    <div className="flex items-center justify-between mb-4">
                      <Dumbbell className="text-blue-400 group-hover:text-blue-300 transition-colors" size={40} />
                      <span className="bg-blue-500/30 text-blue-200 px-3 py-1 rounded-full text-sm font-semibold">
                        {workout.level}
                      </span>
                    </div>
                    <h3 className="text-2xl font-bold mb-4 group-hover:text-blue-300 transition-colors">{workout.name}</h3>
                    <div className="space-y-2 text-gray-300 mb-6">
                      <div className="flex items-center gap-2">
                        <Clock size={18} />
                        <span>{workout.duration}</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Flame size={18} />
                        <span>{workout.calories} kcal</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Award size={18} />
                        <span>Difficulty: {workout.difficulty}</span>
                      </div>
                    </div>
                    <button className="w-full bg-blue-500 hover:bg-blue-600 py-3 rounded-lg transition-all font-bold flex items-center justify-center gap-2">
                      विस्तार देखें →
                    </button>
                  </div>
                ))}
              </div>
            ) : (
              <div className="bg-gradient-to-br from-blue-500/10 to-purple-500/10 border border-blue-500/30 rounded-2xl p-10">
                <button
                  onClick={() => setSelectedWorkout(null)}
                  className="mb-8 text-blue-400 hover:text-blue-300 font-semibold flex items-center gap-2 group transition-all"
                >
                  <span className="group-hover:-translate-x-2 transition-transform">←</span> वापस जाएं
                </button>
                <div className="flex justify-between items-start mb-8">
                  <div>
                    <h3 className="text-5xl font-bold mb-4">{selectedWorkout.name}</h3>
                    <div className="flex gap-4 flex-wrap">
                      <span className="bg-blue-500/30 px-4 py-2 rounded-full">⏱️ {selectedWorkout.duration}</span>
                      <span className="bg-purple-500/30 px-4 py-2 rounded-full">🔥 {selectedWorkout.calories} cal</span>
                      <span className="bg-yellow-500/30 px-4 py-2 rounded-full">💪 {selectedWorkout.difficulty}</span>
                    </div>
                  </div>
                </div>

                <div className="space-y-4">
                  <h4 className="text-2xl font-bold mb-6">🏋️ Exercises:</h4>
                  {selectedWorkout.exercises.map((ex, i) => (
                    <div key={i} className="bg-black/30 rounded-xl p-6 border border-blue-500/20 hover:border-blue-500/50 transition-all">
                      <h5 className="text-xl font-bold mb-4 text-blue-300">{i + 1}. {ex.name}</h5>
                      <div className="grid md:grid-cols-3 gap-4 text-gray-300">
                        {ex.sets && (
                          <div className="bg-blue-500/10 rounded-lg p-3">
                            <span className="text-sm text-gray-400">Sets × Reps</span>
                            <p className="text-lg font-bold">{ex.sets} × {ex.reps}</p>
                          </div>
                        )}
                        {ex.rest && (
                          <div className="bg-purple-500/10 rounded-lg p-3">
                            <span className="text-sm text-gray-400">Rest Time</span>
                            <p className="text-lg font-bold">{ex.rest}</p>
                          </div>
                        )}
                        {ex.duration && (
                          <div className="bg-green-500/10 rounded-lg p-3">
                            <span className="text-sm text-gray-400">Duration</span>
                            <p className="text-lg font-bold">{ex.duration}</p>
                          </div>
                        )}
                        {ex.intensity && (
                          <div className="bg-orange-500/10 rounded-lg p-3">
                            <span className="text-sm text-gray-400">Intensity</span>
                            <p className="text-lg font-bold">{ex.intensity}</p>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </div>

                <div className="mt-10 bg-blue-600/20 border border-blue-500/30 rounded-xl p-6">
                  <h4 className="text-xl font-bold mb-3">💡 Tips:</h4>
                  <ul className="space-y-2 text-gray-300">
                    <li>✅ सही form के साथ exercise करें - जल्दबाज़ी न करें</li>
                    <li>✅ पहले warm-up करना न भूलें</li>
                    <li>✅ हर set के बीच rest लें</li>
                    <li>✅ Breathing को control में रखें - breath hold न करें</li>
                    <li>✅ अगर pain महसूस हो तो तुरंत रोक दें</li>
                  </ul>
                </div>
              </div>
            )}
          </div>
        )}

        {/* ==================== NUTRITION TAB ==================== */}
        {activeTab === 'nutrition' && (
          <div className="space-y-8">
            <div>
              <h2 className="text-5xl font-bold mb-3">🥗 Nutrition Plans</h2>
              <p className="text-gray-400">सही nutrition बिना फायदेमंद नहीं है - proper diet लें</p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {nutritionPlans.map((tip, i) => (
                <div
                  key={i}
                  className="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-2xl p-8 hover:border-green-500/60 hover:shadow-lg hover:shadow-green-500/20 transition-all group"
                >
                  <div className="text-6xl mb-4 group-hover:scale-125 transition-transform">{tip.icon}</div>
                  <h3 className="text-2xl font-bold mb-3 text-green-300">{tip.title}</h3>
                  <p className="text-gray-300 mb-6 leading-relaxed">{tip.description}</p>
                  <div className="space-y-2">
                    <p className="text-sm font-semibold text-green-400">Best sources:</p>
                    <div className="flex flex-wrap gap-2">
                      {tip.tips.map((t, idx) => (
                        <span key={idx} className="bg-green-500/20 text-green-200 px-3 py-1 rounded-full text-sm">
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Nutrition Schedule */}
            <div className="bg-gradient-to-br from-orange-500/10 to-red-500/10 border border-orange-500/30 rounded-2xl p-8">
              <h3 className="text-3xl font-bold mb-8 flex items-center gap-3">
                ⏰ Eating Schedule (दिन भर खाना)
              </h3>
              <div className="grid md:grid-cols-5 gap-4">
                {[
                  { time: '6-7 AM', meal: 'Breakfast', food: 'Eggs, Oats, Milk' },
                  { time: '10 AM', meal: 'Mid-Morning', food: 'Banana, Almonds' },
                  { time: '1-2 PM', meal: 'Lunch', food: 'Rice, Chicken, Vegetables' },
                  { time: '4-5 PM', meal: 'Snack', food: 'Greek Yogurt, Berries' },
                  { time: '7-8 PM', meal: 'Dinner', food: 'Fish/Chicken, Brown Rice' }
                ].map((item, i) => (
                  <div key={i} className="bg-black/30 rounded-xl p-6 border border-orange-500/20">
                    <p className="text-orange-400 font-bold text-sm mb-2">{item.time}</p>
                    <h4 className="text-lg font-bold mb-2">{item.meal}</h4>
                    <p className="text-gray-400 text-sm">{item.food}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Daily Hydration */}
            <div className="bg-gradient-to-br from-cyan-500/10 to-blue-500/10 border border-cyan-500/30 rounded-2xl p-8">
              <h3 className="text-3xl font-bold mb-6 flex items-center gap-3">
                💧 Daily Hydration Target
              </h3>
              <div className="grid md:grid-cols-4 gap-4">
                {['Morning', 'Afternoon', 'Evening', 'Night'].map((period, i) => (
                  <div key={i} className="bg-black/30 rounded-xl p-6 border border-cyan-500/20 text-center">
                    <p className="text-cyan-400 font-bold mb-2">{period}</p>
                    <p className="text-3xl font-bold text-white">1L</p>
                    <p className="text-gray-400 text-sm mt-2">4 glasses</p>
                  </div>
                ))}
              </div>
              <p className="text-gray-300 mt-6 text-center bg-blue-500/10 rounded-lg p-4">
                📌 कुल = 4 लीटर पानी रोज़ = सुस्वास्थ्य का गोल्डन रूल
              </p>
            </div>
          </div>
        )}

        {/* ==================== PROGRESS TAB ==================== */}
        {activeTab === 'progress' && (
          <div className="space-y-8">
            <div>
              <h2 className="text-5xl font-bold mb-3">📊 Progress Tracker</h2>
              <p className="text-gray-400">अपना progress track करें और motivated रहें</p>
            </div>

            {/* Weight Input */}
            <div className="bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/30 rounded-2xl p-8">
              <h3 className="text-3xl font-bold mb-8 flex items-center gap-3">
                ⚖️ Weight Tracker
              </h3>
              <div className="flex gap-4 mb-8 flex-col sm:flex-row">
                <input
                  type="number"
                  placeholder="अपना weight डालें (kg)"
                  value={weight}
                  onChange={(e) => setWeight(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleAddProgress()}
                  className="flex-1 bg-black/30 border border-purple-500/30 rounded-xl px-6 py-4 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/50 transition-all text-lg"
                />
                <button
                  onClick={handleAddProgress}
                  className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 px-8 py-4 rounded-xl transition-all font-bold text-lg shadow-lg hover:shadow-purple-500/50 whitespace-nowrap"
                >
                  ➕ Add Weight
                </button>
              </div>

              {/* Stats */}
              {stats && (
                <div className="grid md:grid-cols-5 gap-4 mb-8">
                  <div className="bg-black/30 rounded-xl p-4 border border-purple-500/20">
                    <p className="text-purple-400 text-sm font-semibold mb-1">Current</p>
                    <p className="text-3xl font-bold">{stats.current} kg</p>
                  </div>
                  <div className="bg-black/30 rounded-xl p-4 border border-pink-500/20">
                    <p className="text-pink-400 text-sm font-semibold mb-1">Starting</p>
                    <p className="text-3xl font-bold">{stats.initial} kg</p>
                  </div>
                  <div className={`bg-black/30 rounded-xl p-4 border ${stats.change < 0 ? 'border-green-500/20' : 'border-red-500/20'}`}>
                    <p className={`text-sm font-semibold mb-1 ${stats.change < 0 ? 'text-green-400' : 'text-red-400'}`}>
                      Progress
                    </p>
                    <p className={`text-3xl font-bold ${stats.change < 0 ? 'text-green-400' : 'text-red-400'}`}>
                      {stats.change} kg
                    </p>
                  </div>
                  <div className="bg-black/30 rounded-xl p-4 border border-yellow-500/20">
                    <p className="text-yellow-400 text-sm font-semibold mb-1">Max</p>
                    <p className="text-3xl font-bold">{stats.max} kg</p>
                  </div>
                  <div className="bg-black/30 rounded-xl p-4 border border-blue-500/20">
                    <p className="text-blue-400 text-sm font-semibold mb-1">Min</p>
                    <p className="text-3xl font-bold">{stats.min} kg</p>
                  </div>
                </div>
              )}
            </div>

            {/* Progress History */}
            {progressData.length > 0 && (
              <div className="bg-gradient-to-br from-indigo-500/10 to-blue-500/10 border border-indigo-500/30 rounded-2xl p-8">
                <h3 className="text-3xl font-bold mb-8 flex items-center gap-3">
                  📈 Your Progress History
                </h3>
                <div className="space-y-3 max-h-96 overflow-y-auto">
                  {[...progressData].reverse().map((data, i) => (
                    <div
                      key={i}
                      className="bg-black/30 rounded-xl p-5 border border-indigo-500/20 flex justify-between items-center hover:border-indigo-500/50 transition-all group"
                    >
                      <div className="flex-1">
                        <p className="text-indigo-400 font-bold">{data.date}</p>
                        <p className="text-gray-400 text-sm">{data.time}</p>
                      </div>
                      <div className="text-center">
                        <p className="text-3xl font-bold text-indigo-300">{data.weight}</p>
                        <p className="text-gray-400 text-sm">kg</p>
                      </div>
                      <button
                        onClick={() => handleDeleteProgress(progressData.length - 1 - i)}
                        className="ml-4 text-red-400 hover:text-red-300 opacity-0 group-hover:opacity-100 transition-opacity font-bold"
                      >
                        ✕
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Fitness Tips */}
            <div className="grid md:grid-cols-2 gap-6">
              <div className="bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-2xl p-8">
                <h3 className="text-2xl font-bold mb-6 flex items-center gap-2">
                  💡 Daily Tips
                </h3>
                <ul className="space-y-3 text-gray-300">
                  <li className="flex items-start gap-3">
                    <span className="text-yellow-400 font-bold">✅</span>
                    <span>हर रोज़ कम से कम 30 मिनट व्यायाम करें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-yellow-400 font-bold">✅</span>
                    <span>सुबह 6-7 बजे उठने की कोशिश करें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-yellow-400 font-bold">✅</span>
                    <span>खाना धीरे-धीरे चबाकर खाएं</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-yellow-400 font-bold">✅</span>
                    <span>रात को 8 घंटे की नींद लें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-yellow-400 font-bold">✅</span>
                    <span>हर दिन कम से कम 3-4 लीटर पानी पिएं</span>
                  </li>
                </ul>
              </div>

              <div className="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-2xl p-8">
                <h3 className="text-2xl font-bold mb-6 flex items-center gap-2">
                  🏆 Motivation Tips
                </h3>
                <ul className="space-y-3 text-gray-300">
                  <li className="flex items-start gap-3">
                    <span className="text-green-400 font-bold">🎯</span>
                    <span>एक realistic goal सेट करें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-green-400 font-bold">🎯</span>
                    <span>एक workout buddy ढूंढें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-green-400 font-bold">🎯</span>
                    <span>Progress को celebrate करें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-green-400 font-bold">🎯</span>
                    <span>गलतियों से सीखें, हार न मानें</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-green-400 font-bold">🎯</span>
                    <span>हर हफ्ते अपने आप को reward दें</span>
                  </li>
                </ul>
              </div>
            </div>

            {/* No Data Message */}
            {progressData.length === 0 && (
              <div className="bg-gradient-to-br from-gray-700/20 to-gray-600/20 border border-gray-500/30 rounded-2xl p-12 text-center">
                <p className="text-gray-400 text-lg mb-4">अभी कोई data नहीं है</p>
                <p className="text-gray-500">अपना weight enter करें और track करना शुरु करें!</p>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-black/50 border-t border-blue-500/20 mt-16 py-8">
        <div className="max-w-7xl mx-auto px-4 text-center text-gray-400">
          <p>💪 Made with ❤️ for Your Fitness Journey | © 2024 FitPro</p>
          <p className="mt-2 text-sm">Remember: Consistency is key to success! 🚀</p>
        </div>
      </footer>
    </div>
  );
}



