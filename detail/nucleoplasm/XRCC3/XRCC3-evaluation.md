---
type: protein-evaluation
gene: "XRCC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XRCC3 — REJECTED (研究热度过高 (PubMed strict=589，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XRCC3 |
| 蛋白名称 | DNA repair protein XRCC3 |
| 蛋白大小 | 346 aa / 37.9 kDa |
| UniProt ID | O43542 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Mitochond |
| 蛋白大小 | 10/10 | ×1 | 10 | 346 aa / 37.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=589 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016467, IPR058766, IPR027417, IPR013632, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- Rad51C-XRCC3 complex (GO:0033065)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 589 |
| PubMed broad count | 981 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RAD51 Paralogs and RAD51 Paralog Complexes BCDX2 and CX3 Interact with BRCA2.. *bioRxiv : the preprint server for biology*. PMID: 39416194
2. DNA repair gene XRCC3 Thr241Met polymorphisms and lung cancer risk: a meta-analysis.. *Bulletin du cancer*. PMID: 25794597
3. Gene polymorphisms and risk of head and neck squamous cell carcinoma: a systematic review.. *Reports of practical oncology and radiotherapy : journal of Greatpoland Cancer Center in Poznan and Polish Society of Radiation Oncology*. PMID: 36632298
4. DNA repair gene XRCC3 polymorphisms and bladder cancer risk: a meta-analysis.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 24104500
5. DNA repair gene XRCC3 Thr241Met polymorphism and hepatocellular carcinoma risk.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 23824570

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.3，有序区 87.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016467, IPR058766, IPR027417, IPR013632, IPR020588; Pfam: PF26169, PF08423 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA2 | 0.999 | 0.886 | — |
| XRCC2 | 0.999 | 0.130 | — |
| RAD51C | 0.999 | 0.988 | — |
| RAD51 | 0.998 | 0.955 | — |
| RAD51B | 0.985 | 0.496 | — |
| FANCG | 0.984 | 0.625 | — |
| RAD51D-2 | 0.983 | 0.496 | — |
| RAD52 | 0.978 | 0.767 | — |
| RAD51D | 0.978 | 0.496 | — |
| WRN | 0.964 | 0.605 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG11892 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| spn-B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| rols | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rpt6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ogl | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fadB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| TOR1AIP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5AR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INSYN2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.3 + PDB: 无 | pLDDT=87.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. XRCC3 — DNA repair protein XRCC3，研究基础较多，新颖性有限。
2. 蛋白大小346 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 589 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 589 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43542
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126215-XRCC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XRCC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43542
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/XRCC3/IF_images/XRCC3_IF_red_green.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/XRCC3/XRCC3-PAE.png]]
