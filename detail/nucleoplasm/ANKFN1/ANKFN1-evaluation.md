---
type: protein-evaluation
gene: "ANKFN1"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKFN1

Q8N957 | Ankyrin repeat and fibronectin type-III domain-containing protein 1 | 1146aa | pLDDT 65.8 | PM=14 | norm=67.2/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 |
| 蛋白大小 | 10/10 | ×1 | 10 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 4/10 | ×3 | 12 |
| 调控结构域 | 5/10 | ×2 | 10 |
| PPI 网络 | 3/10 | ×3 | 9 |
| **加权总分** | | | **123/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 14 | | |
| **归一化总分 (÷1.83)** | | | **67.2/100** |

**UniProt**: Q8N957 — No explicit subcellular location annotations in UniProt (subcellular_locations empty). GO-CC: spindle (IBA:GO_Central). Note: UniProt lacks nucleus/nucleoplasm annotation despite HPA data to the contrary; this discrepancy may reflect limited experimental characterization of this protein.

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm (Approved)，额外定位 Plasma membrane。UniProt GO-CC 仅有 spindle 条目，缺乏核定位注释，但 HPA IF reliability 为 Approved 级别且 Nucleoplasm 列为主定位，核定位证据主要来源于 HPA 免疫荧光数据。因同时存在 Plasma membrane 信号，核定位特异性评为 8/10。

### 蛋白大小
1146 aa，129.7 kDa，属于大型蛋白。由 6 个 InterPro 条目构成，包含多个 Ankyrin repeat (IPR002110/IPR036770) 和 Fibronectin type-III 结构域 (IPR003961/IPR036116/IPR013783)。大分子量有利于结构域辨识和生化操作，评为 10/10。

### 研究新颖性
PubMed strict count = 14（≤20 档），研究极为稀少。关键文献聚焦于神经元功能：PMID 39303704 报道 ANKFN1（mWake）在杏仁核振荡器调控细胞与行为节律中的作用，PMID 33140455 表征 mWake 在小鼠脑中的表达模式。此外 PMID 36533556 涉及斑马鱼纤毛过渡区突变体表型分析，PMID 37895191 关联韩牛胴体性状的错义变异。总体研究集中在神经生物学和遗传关联层面，无深度生化或结构研究。评为 10/10（高新颖性）。

### PDB 结构
**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。
AlphaFold v6: mean_pLDDT = 65.8，pct_gt_90 = 36.0%，pct_70_90 = 18.7%，pct_lt_50 = 40.8%。近 41% 残基置信度低于 50，提示存在显著无序区域。无实验 PDB 结构。整体结构可信度中等偏下。评为 4/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110, IPR036770)、Fibronectin type-III (IPR003961, IPR036116, IPR013783)、以及 uncharacterized IPR039269。Pfam: Fibronectin type-III domain (PF00041)。ANK 重复为蛋白-蛋白相互作用支架，FN3 结构域常见于细胞表面受体和细胞粘附分子，组合具有一定调控潜力。评为 5/10。

### PPI 网络
STRING: 15 个互作伙伴，最高分 0.611（TTLL9），多数为 textmining 来源的低置信互作（0.4-0.6 区间）。排名靠前的伙伴：TTLL9 (0.611, 微管蛋白连接酶)、C2orf81 (0.600)、CEP72 (0.594, 中心体蛋白)、CCDC175 (0.594)。IntAct: 无实验互作记录。UniProt: 无 curated interaction。整体 PPI 网络弱，缺乏实验验证的蛋白互作，表明该蛋白的互作组信息尚不完善。评为 3/10。

### 关键文献
- PMID 39303704: mWake/ANKFN1 在杏仁核振荡器调控节律中的作用 (Neuron, 2024)
- PMID 33140455: Characterization of mWake expression in the murine brain (J Comp Neurol, 2021)
- PMID 36533556: Variable phenotypes in zebrafish ciliary transition zone mutants (Dis Model Mech, 2022)

### 人工复核建议
核定位主要依赖 HPA Approved 级别的 Nucleoplasm 注释，UniProt 自身缺乏核定位数据，建议交叉验证 HPA IF 原图（如可获取）。PubMed 严格计数 14 确认了极高新颖性，该蛋白作为 mWake 在神经节律调控中的角色值得关注，但与 TE 调控的直接关联尚不明确。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000153930-ANKFN1/subcellular

![](https://images.proteinatlas.org/48953/1797_C1_32_red_green.jpg)
![](https://images.proteinatlas.org/48953/1797_C1_33_red_green.jpg)
![](https://images.proteinatlas.org/48953/1886_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/48953/1886_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/48953/1891_M16_18_cr5bbdb8434118b_red_green.jpg)
![](https://images.proteinatlas.org/48953/1891_M16_25_cr5bbdb84342f64_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N957-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
