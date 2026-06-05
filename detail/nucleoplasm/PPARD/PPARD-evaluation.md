---
type: protein-evaluation
gene: "PPARD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PPARD — REJECTED (研究热度过高 (PubMed strict=321，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPARD / NR1C2, PPARB |
| 蛋白名称 | Peroxisome proliferator-activated receptor delta |
| 蛋白大小 | 441 aa / 49.9 kDa |
| UniProt ID | Q03181 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 49.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=321 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.9; PDB: 1GWX, 1Y0S, 2AWH, 2B50, 2BAW, 2ENV, 2GWX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003074, IPR003075, IPR035500, IPR000536, IPR050 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 321 |
| PubMed broad count | 506 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1C2, PPARB |

**关键文献**:
1. The ménage à trois of autophagy, lipid droplets and liver disease.. *Autophagy*. PMID: 33794741
2. Gut Microbiota-Derived Butyrate Induces Epigenetic and Metabolic Reprogramming in Myeloid-Derived Suppressor Cells to Alleviate Primary Biliary Cholangitis.. *Gastroenterology*. PMID: 38810839
3. Endothelial PPARδ Ablation Exacerbates Vascular Hyperpermeability via STAT1/CXCL10 Signaling in Acute Lung Injury.. *Circulation research*. PMID: 39996324
4. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
5. Jieyu Guben decoction alleviates combined allergic rhinitis and asthma syndrome by balancing Th17/Treg expression and restoring PPARD.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 40031093

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| 可用 PDB 条目 | 1GWX, 1Y0S, 2AWH, 2B50, 2BAW, 2ENV, 2GWX, 2J14, 2Q5G, 2XYJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1GWX, 1Y0S, 2AWH, 2B50, 2BAW, 2ENV, 2GWX, 2J14, 2Q5G, 2XYJ）+ AlphaFold极高置信度预测（pLDDT=82.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003074, IPR003075, IPR035500, IPR000536, IPR050234; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ncor1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22078881|imex:IM-16633 |
| PRKAA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11910|pubmed:18674809 |
| PRKAA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11910|pubmed:18674809 |
| HDAC2 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NCOA1 | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| PPARGC1A | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| CREBBP | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| NCOA2 | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| EBI-12596549 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:21775429|imex:IM-25604 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 1GWX, 1Y0S, 2AWH, 2B50, 2BAW,  | pLDDT=82.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. PPARD — Peroxisome proliferator-activated receptor delta，研究基础较多，新颖性有限。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 321 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 321 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03181
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112033-PPARD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPARD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03181
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q03181-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
