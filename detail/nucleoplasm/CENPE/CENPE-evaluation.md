---
type: protein-evaluation
gene: "CENPE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CENPE — REJECTED (研究热度过高 (PubMed strict=382，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPE |
| 蛋白名称 | Centromere-associated protein E |
| 蛋白大小 | 2701 aa / 316.4 kDa |
| UniProt ID | Q02224 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Microtubules; 额外: Cytokinetic bridge, Mitotic spindle; UniProt: Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton |
| 蛋白大小 | 2/10 | ×1 | 2 | 2701 aa / 316.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=382 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.4; PDB: 1T5C, 5JVP, 6M4I, 8HFH, 8OWI, 8WHL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027640, IPR019821, IPR001752, IPR036961, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Cytokinetic bridge, Mitotic spindle | Supported |
| UniProt | Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spindle; Chromosome, centromere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- condensed chromosome, centromeric region (GO:0000779)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- kinetochore (GO:0000776)
- kinetochore microtubule (GO:0005828)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 382 |
| PubMed broad count | 520 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mutations in the spliceosomal gene SNW1 cause neurodevelopment disorders with microcephaly.. *The Journal of clinical investigation*. PMID: 40608414
2. Primary microcephaly gene CENPE is a novel biomarker and potential therapeutic target for non-WNT/non-SHH medulloblastoma.. *Frontiers in immunology*. PMID: 37593739
3. Kinesins and cancer.. *Nature reviews. Cancer*. PMID: 22825217
4. CENPE is a diagnostic and prognostic biomarker for cervical cancer.. *Heliyon*. PMID: 39759304
5. Analyzing the expression and clinical significance of CENPE in gastric cancer.. *BMC medical genomics*. PMID: 38702677

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.4 |
| 高置信度残基 (pLDDT>90) 占比 | 5.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.7% |
| 中等置信 (pLDDT 50-70) 占比 | 36.5% |
| 低置信 (pLDDT<50) 占比 | 42.5% |
| 有序区域 (pLDDT>70) 占比 | 21.0% |
| 可用 PDB 条目 | 1T5C, 5JVP, 6M4I, 8HFH, 8OWI, 8WHL |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.4），有序残基占 21.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027640, IPR019821, IPR001752, IPR036961, IPR027417; Pfam: PF00225 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BUB1B | 0.999 | 0.636 | — |
| CENPF | 0.999 | 0.230 | — |
| NUF2 | 0.996 | 0.484 | — |
| CENPA | 0.993 | 0.052 | — |
| BUB1 | 0.991 | 0.259 | — |
| PRC1 | 0.990 | 0.633 | — |
| CDC20 | 0.989 | 0.049 | — |
| KIF11 | 0.988 | 0.305 | — |
| KIF2C | 0.988 | 0.068 | — |
| KIF18A | 0.985 | 0.079 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000265148.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9763420|imex:IM-18999 |
| Q8BWX6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CENPF | psi-mi:"MI:0018"(two hybrid) | pubmed:9763420|imex:IM-18999 |
| BUB1B | psi-mi:"MI:0018"(two hybrid) | pubmed:9763420|imex:IM-18999 |
| NUF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17535814|imex:IM-20014 |
| NDC80 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:17535814|imex:IM-20014 |
| TP63 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20085233|imex:IM-20439 |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| RPL21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.4 + PDB: 1T5C, 5JVP, 6M4I, 8HFH, 8OWI,  | pLDDT=54.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome, centromere, kinetochore; Cytoplasm, cy / Microtubules; 额外: Cytokinetic bridge, Mitotic spin | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CENPE — Centromere-associated protein E，研究基础较多，新颖性有限。
2. 蛋白大小2701 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 382 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 382 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02224
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138778-CENPE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02224
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
