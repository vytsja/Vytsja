  <div className="flex justify-between items-center mb-4">
    <button
      className="bg-blue-600 text-white px-4 py-2 rounded shadow"
      onClick={addWeek}
    >
      Додати новий тиждень
    </button>
    <select
      value={currentWeekIdx}
      onChange={e => setCurrentWeekIdx(Number(e.target.value))}
      className="border rounded px-2 py-1"
    >
      {weeks.map((w, i) => (
        <option key={i} value={i}>
          {w.startDate ? `Тиждень з ${w.startDate}` : `Тиждень ${i + 1}`}
        </option>
      ))}
    </select>
  </div>

  {weeks[currentWeekIdx] ? (
    <FinanceChecklistApp
      data={weeks[currentWeekIdx]}
      setData={d =>
        setWeeks(ws => ws.map((w, i) => (i === currentWeekIdx ? d : w)))
      }
    />
  ) : (
    <div className="text-slate-400 text-center">Виберіть або додайте тиждень.</div>
  )}
</div>
