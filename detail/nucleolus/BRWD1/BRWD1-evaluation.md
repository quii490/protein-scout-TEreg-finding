---
type: protein-evaluation
gene: "BRWD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRWD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRWD1 / C21orf107, WDR9 |
| 蛋白名称 | Bromodomain and WD repeat-containing protein 1 |
| 蛋白大小 | 2320 aa / 262.9 kDa |
| UniProt ID | Q9NSI6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli, Vesicles, Plasma membran; UniProt: Cytoplasm; Nucleus; Cell projection, cilium membrane; Cytopl |
| 蛋白大小 | 2/10 | ×1 | 2 | 2320 aa / 262.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.6; PDB: 3Q2E |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052060, IPR001487, IPR036427, IPR018359, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli, Vesicles, Plasma membrane, Mitotic spindle | Approved |
| UniProt | Cytoplasm; Nucleus; Cell projection, cilium membrane; Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- ciliary membrane (GO:0060170)
- cytosol (GO:0005829)
- motile cilium (GO:0031514)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf107, WDR9 |

**关键文献**:
1. MALAT1 promotes cisplatin resistance in cervical cancer by activating the PI3K/AKT pathway.. *European review for medical and pharmacological sciences*. PMID: 30536307
2. Chemoselective Tagging of Protein Methacrylation.. *Journal of the American Chemical Society*. PMID: 41218107
3. BRWD1 orchestrates small pre-B cell chromatin topology by converting static to dynamic cohesin.. *Nature immunology*. PMID: 37985858
4. Mouse BRWD1 is critical for spermatid postmeiotic transcription and female meiotic chromosome stability.. *The Journal of cell biology*. PMID: 25547156
5. Rescue of deficits by Brwd1 copy number restoration in the Ts65Dn mouse model of Down syndrome.. *Nature communications*. PMID: 36289231

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.6 |
| 高置信度残基 (pLDDT>90) 占比 | 10.9% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 51.4% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 3Q2E |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.6），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052060, IPR001487, IPR036427, IPR018359, IPR057451; Pfam: PF00439, PF25437, PF25313 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCA4 | 0.949 | 0.314 | — |
| STAT5A | 0.766 | 0.000 | — |
| STAT5B | 0.759 | 0.000 | — |
| H3C12 | 0.750 | 0.091 | — |
| H3C13 | 0.750 | 0.091 | — |
| UBXN7 | 0.702 | 0.593 | — |
| CUL4A | 0.623 | 0.585 | — |
| PSMG1 | 0.604 | 0.000 | — |
| RAG2 | 0.556 | 0.000 | — |
| DDB1 | 0.554 | 0.513 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Smarca4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12889071 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| UBXN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| Q0WJ06 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ITGB1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.6 + PDB: 3Q2E | pLDDT=55.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell projection, cilium membra / Nucleoplasm, Cytosol; 额外: Nucleoli, Vesicles, Plas | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BRWD1 — Bromodomain and WD repeat-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小2320 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSI6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185658-BRWD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRWD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSI6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
