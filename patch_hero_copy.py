from pathlib import Path

path = Path('/home/ubuntu/swapphone/client/src/App.tsx')
text = path.read_text()
replacements = {
    '>Shop phones <ArrowRight className="ml-2 inline" size={15}/></button>': '>Shop checked phones <ArrowRight className="ml-2 inline" size={15}/></button>',
    'md:border-[#cfd2cb] md:bg-transparent md:px-6 md:py-3.5 md:text-sm">Sell your phone</button>': 'md:border-[#cfd2cb] md:bg-transparent md:px-6 md:py-3.5 md:text-sm">Get a value for your phone</button>',
    'A clear estimate for the phone you’re ready to leave behind': 'Find out what your phone is worth',
    'Share a few details. We’ll estimate the value and guide you to the next step with one simple contact path.': 'Choose your model, tell us its condition, and get a clear estimate before you contact us. No guesswork, no long form.',
    '>Get my estimate <ArrowRight className="ml-2 inline" size={15}/></button>': '>See my estimate <ArrowRight className="ml-2 inline" size={15}/></button>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Missing expected copy: {old}')
    text = text.replace(old, new, 1)
path.write_text(text)
print('Applied hero copy replacements:', len(replacements))
