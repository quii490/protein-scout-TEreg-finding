---
type: protein-evaluation
gene: "TRAF6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TRAF6 — REJECTED (研究热度过高 (PubMed strict=2595，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAF6 / RNF85 |
| 蛋白名称 | TNF receptor-associated factor 6 |
| 蛋白大小 | 522 aa / 59.6 kDa |
| UniProt ID | Q9Y4K3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoli; UniProt: Cytoplasm; Cytoplasm, cell cortex; Nucleus; Lipid droplet |
| 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 59.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2595 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.2; PDB: 1LB4, 1LB5, 1LB6, 2ECI, 2JMD, 3HCS, 3HCT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002083, IPR012227, IPR008974, IPR049342, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli | Uncertain |
| UniProt | Cytoplasm; Cytoplasm, cell cortex; Nucleus; Lipid droplet | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CD40 receptor complex (GO:0035631)
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- extrinsic component of cytoplasmic side of plasma membrane (GO:0031234)
- glutamatergic synapse (GO:0098978)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2595 |
| PubMed broad count | 4191 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF85 |

**关键文献**:
1. TRAF6 enhances PD-L1 expression through YAP1-TFCP2 signaling in melanoma.. *Cancer letters*. PMID: 38583649
2. Sufu limits sepsis-induced lung inflammation via regulating phase separation of TRAF6.. *Theranostics*. PMID: 37441604
3. TRAF6 inhibits colorectal cancer metastasis through regulating selective autophagic CTNNB1/β-catenin degradation and is targeted for GSK3B/GSK3β-mediated phosphorylation and degradation.. *Autophagy*. PMID: 30806153
4. Inhibition of TRAF6 ubiquitin-ligase activity by PRDX1 leads to inhibition of NFKB activation and autophagy activation.. *Autophagy*. PMID: 29929436
5. Non-canonical Activation of the DNA Sensing Adaptor STING by ATM and IFI16 Mediates NF-κB Signaling after Nuclear DNA Damage.. *Molecular cell*. PMID: 30193098

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 1LB4, 1LB5, 1LB6, 2ECI, 2JMD, 3HCS, 3HCT, 3HCU, 4Z8M, 5ZUJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1LB4, 1LB5, 1LB6, 2ECI, 2JMD, 3HCS, 3HCT, 3HCU, 4Z8M, 5ZUJ）+ AlphaFold极高置信度预测（pLDDT=84.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002083, IPR012227, IPR008974, IPR049342, IPR037309; Pfam: PF21355, PF18048, PF13923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MALT1 | 0.999 | 0.835 | — |
| TLR4 | 0.999 | 0.923 | — |
| TIFA | 0.999 | 0.976 | — |
| IRF7 | 0.999 | 0.838 | — |
| MYD88 | 0.999 | 0.849 | — |
| TBK1 | 0.999 | 0.994 | — |
| TLR3 | 0.999 | 0.985 | — |
| IRF5 | 0.999 | 0.515 | — |
| TAB3 | 0.999 | 0.848 | — |
| CD40 | 0.999 | 0.895 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000433623.1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-88690 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ecsit | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Irak1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Traf3ip2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Bag6 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Fhl1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pxn | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Calr | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| TNFAIP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11463333 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 1LB4, 1LB5, 1LB6, 2ECI, 2JMD,  | pLDDT=84.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cell cortex; Nucleus; Lipid  / Mitochondria; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TRAF6 — TNF receptor-associated factor 6，研究基础较多，新颖性有限。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2595 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2595 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4K3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175104-TRAF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4K3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
