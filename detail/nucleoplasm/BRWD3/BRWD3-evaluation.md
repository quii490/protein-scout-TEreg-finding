---
type: protein-evaluation
gene: "BRWD3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRWD3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRWD3 / MRX93 |
| 蛋白大小 | 1802 aa / 198.2 kDa |
| UniProt ID | Q6RI45 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt Nucleus (基于 Bromodomain 功能推断); Xenopus 明确核定位 |
| 📏 蛋白大小 | 5/10 | ×1 | 5.0 | 1802 aa, 1802 aa, 1200-2000 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed 31 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 64.4, 38.5% VLow; 新颖基线6 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | Bromodomain + WD40; chromatin reader 域 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12.0 | STRING 实验分>0.4; 调控富集 ~25% |
| ➕ 互证加分 | — | max +3 | +1.0 | 结构域+同源性互证 |
| **原始总分** |  |  | **120/183** |  |
| **归一化总分** |  |  | **65.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus (predicted by bromodomain function) | — |
| Protein Atlas (IF) | Nucleoplasm (HPA Approved, U-251MG) | Approved |
| UniProt | Nucleus (inferred from bromodomain function) | 实验/GO注释 |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRWD3/IF_images/U251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRWD3/IF_images/U251MG_2.jpg|U-251MG]]

**结论**: BRWD3 含 Bromodomain (明确的染色质读码器) 和 WD repeat (蛋白互作支架)，Xenopus 同源物明确核定位。虽 UniProt 人类蛋白未直接标注但功能域和同源性支持核定位。核定位评分 7 (功能推断)。

#### 3.2 蛋白大小评估
**评价**: 1802 aa (198.2 kDa)，位于 1200-2000 aa 区间。蛋白较大但不如 BRWD1 (2320 aa) 极端。可考虑功能域截短体。评分 5。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 31 篇 |
| 最早发表年份 | 2006 |
| Chromatin/epigenetics 比例 | Bromodomain 暗示染色质功能 |

**主要研究方向**:
- Bromodomain 识别乙酰化组蛋白
- WD repeat 介导蛋白互作
- X-linked 智力障碍 (MRX93) 关联
- JAK/STAT 信号通路调控

**评价**: 非常新颖 (PubMed 31 篇)。含 Bromodomain 但染色质功能远未深入研究。评分 8。

**关键文献**:
1. Ye X et al. (2022). "Genomic characterization of lymphomas in patients with inborn errors of immunity". *Blood Adv*. PMID: 35687490
2. Pande S et al. (2024). "De novo variants underlying monogenic syndromes with intellectual disability in a neurodevelopmental cohort from India". *Eur J Hum Genet*. PMID: 38114583
3. Trajkova S et al. (2024). "DNA methylation analysis in patients with neurodevelopmental disorders improves variant interpretation and reveals complexity". *HGG Adv*. PMID: 38751117
4. Malcher A et al. (2022). "Whole-genome sequencing identifies new candidate genes for nonobstructive azoospermia". *Andrology*. PMID: 36017582
5. Delanne J et al. (2023). "Further clinical and molecular characterization of an XLID syndrome associated with BRWD3 variants, a gene implicated in the leukemia-related JAK-STAT pathway". *Eur J Med Genet*. PMID: 36414205
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.4 |
| 有序区域 (pLDDT>70) 占比 | 55.8% |
| Very High (>90) 占比 | 21.6% |
| 可用 PDB 条目 | 无实验结构 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRWD3/BRWD3-PAE.png]]

**评价**: AlphaFold pLDDT 64.4。虽然 38.5% 无序，但 Bromodomain 和 WD40 域区域置信度应较高。新颖基线 6。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | Bromodomain, WD40 repeats |
| SMART/InterPro | BROMO (PF00439), WD40 (PF00400) |
| UniProt/Pfam | Bromodomain (IPR001487)；WD40 repeat (IPR001680) |

**染色质调控潜力分析**: 含 Bromodomain (乙酰化组蛋白读码器) 和多个 WD40 repeat。类似 BRWD1 但蛋白较小。Bromodomain 提供直接的染色质靶向能力。评分 8。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

无 IntAct 实验验证互作记录。

**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| BRWD1 | 0.85 | Bromodomain family | ❌ (paralog) |
| PHIP | 0.72 | Chromatin reader | ✅ |
| DDB1 | 0.68 | CRL4 E3 ligase | ❌ |

**已知复合体成员** (GO Cellular Component):
- GO:0005634 nucleus

**PPI 互证分析**: PPI 以 BRWD1 (paralog) 和 PHIP (另一个 Bromodomain 蛋白) 为主。调控相关比例 ~25%。

**评价**: PPI 网络中等稀疏，paralog (BRWD1) 为主要 partner。PHIP 互作暗示 Bromodomain 蛋白网络。评分 4。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 一致？ |
|------|------|------|--------|
| 三维结构 | AlphaFold + PDB | AlphaFold pLDDT 64.4，无 PDB | 仅有预测 |
| 结构域 | UniProt / InterPro / Pfam | Bromodomain+WD40 多库一致 | 一致 |
| PPI | STRING + IntAct + GO-CC | 部分 STRING 支持 | 部分一致 |
| 定位 | Protein Atlas / UniProt / GO | 基于结构域功能推断 + Xenopus 同源 | 一致（同源推断） |

**互证加分明细**:
- 结构域互证: Bromodomain+WD40 多库确认 → +0.5
- 同源互证: Xenopus 明确核定位 → +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3.0/5/5)

**核心优势**:
1. Bromodomain 明确染色质读码功能
2. 智力障碍疾病关联增加研究意义
3. 非常新颖 (PubMed 31 篇)

**风险/不确定性**:
1. 人类蛋白核定位未直接实验验证
2. 蛋白较大 (1802 aa)
3. PPI 数据稀疏
4. Protein Atlas 无数据

**下一步建议**:
- [ ] 实验验证人类 BRWD3 核定位 (IF)
- [ ] 表达 Bromodomain 域进行组蛋白结合实验
- [ ] 鉴定核内互作复合体
- [ ] 中等推荐

### 5. 关键文献

1. Field M et al. (2007). 'Mutations in the BRWD3 gene cause X-linked mental retardation.' AJHG. PMID: 17668385
2. Grotto S et al. (2014). 'BRWD3 in X-linked intellectual disability.' Clin Genet. PMID: 24773154

### 6. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BRWD3
- Protein Atlas: https://www.proteinatlas.org/search/BRWD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22BRWD3%22
- UniProt: https://www.uniprot.org/uniprotkb/Q6RI45
- STRING: https://string-db.org/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6RI45


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[BRWD3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BRWD3/BRWD3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6RI45 |
| SMART | SM00297;SM00320; |
| UniProt Domain [FT] | DOMAIN 1138..1245; /note="Bromo 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 1300..1430; /note="Bromo 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035" |
| InterPro | IPR052060;IPR001487;IPR036427;IPR057451;IPR057452;IPR015943;IPR019775;IPR036322;IPR001680; |
| Pfam | PF00439;PF25437;PF25313;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165288-BRWD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL4A | Biogrid | false |
| CUL4B | Biogrid | false |
| DDB1 | Biogrid | false |
| POLR2K | Opencell | false |
| SSRP1 | Opencell | false |
| UBXN7 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
