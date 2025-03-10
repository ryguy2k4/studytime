rule runall:
    input:
        "results/stackplot_by_class.png",
        "results/barplot_by_weekday.png",
        "results/heatmap_by_weekday.png"

rule prepare_data:
    output: 
        "data/master/studytime.csv"
    shell: 
        "python3 src/data-integration.py"

rule make_stackplot:
    input:
        "data/master/studytime.csv"
    output:
        "results/stackplot_by_class.png"
    shell:
        "python3 src/make-stackplot-by-week.py"

rule make_barplot:
    input:
        "data/master/studytime.csv"
    output:
        "results/barplot_by_weekday.png"
    shell:
        "python3 src/make-barplot-by-weekday.py"

rule make_heatmap:
    input:
        "data/master/studytime.csv"
    output:
        "results/heatmap_by_weekday.png"
    shell:
        "python3 src/make-heatmap-by-weekday.py"