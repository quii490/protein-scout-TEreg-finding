---
type: protein-evaluation
gene: "MALT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MALT1 — REJECTED (研究热度过高 (PubMed strict=629，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MALT1 / MLT |
| 蛋白名称 | Mucosa-associated lymphoid tissue lymphoma translocation protein 1 |
| 蛋白大小 | 824 aa / 92.3 kDa |
| UniProt ID | Q9UDY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Cytosol; UniProt: Cytoplasm, perinuclear region; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 824 aa / 92.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=629 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.5; PDB: 2G7R, 3BFO, 3K0W, 3UO8, 3UOA, 3V4O, 3V55 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029030, IPR052039, IPR011029, IPR007110, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, perinuclear region; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CBM complex (GO:0032449)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- polkadots (GO:0002096)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 629 |
| PubMed broad count | 1100 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MLT |

**关键文献**:
1. Emodin Alleviates Sepsis-Induced Multiorgan Damage by Inhibiting NETosis through Targeting Neutrophils BCL-10.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40779122
2. PRRSV utilizes MALT1-regulated autophagy flux to switch virus spread and reserve.. *Autophagy*. PMID: 39081059
3. The Paracaspase MALT1.. *Biochimie*. PMID: 26386283
4. The Paracaspase MALT1 in Cancer.. *Biomedicines*. PMID: 35203553
5. Germline CBM-opathies: From immunodeficiency to atopy.. *The Journal of allergy and clinical immunology*. PMID: 31060714

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 54.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 2G7R, 3BFO, 3K0W, 3UO8, 3UOA, 3V4O, 3V55, 4I1P, 4I1R, 6F7I |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2G7R, 3BFO, 3K0W, 3UO8, 3UOA, 3V4O, 3V55, 4I1P, 4I1R, 6F7I）+ AlphaFold极高置信度预测（pLDDT=79.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029030, IPR052039, IPR011029, IPR007110, IPR036179; Pfam: PF13895, PF13927, PF18703 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CARD9 | 0.999 | 0.300 | — |
| BCL10 | 0.999 | 0.998 | — |
| TRAF6 | 0.999 | 0.835 | — |
| CARD11 | 0.999 | 0.845 | — |
| CARD10 | 0.999 | 0.100 | — |
| CASP8 | 0.998 | 0.292 | — |
| IKBKG | 0.998 | 0.785 | — |
| IKBKB | 0.985 | 0.314 | — |
| CHUK | 0.968 | 0.071 | — |
| CARD14 | 0.929 | 0.540 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 2G7R, 3BFO, 3K0W, 3UO8, 3UOA,  | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Nucleus / Nucleoli fibrillar center; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MALT1 — Mucosa-associated lymphoid tissue lymphoma translocation protein 1，研究基础较多，新颖性有限。
2. 蛋白大小824 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 629 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 629 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UDY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172175-MALT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MALT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UDY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
