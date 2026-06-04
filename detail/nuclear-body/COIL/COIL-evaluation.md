---
type: protein-evaluation
gene: "COIL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COIL — REJECTED (研究热度过高 (PubMed strict=14551，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COIL / CLN80 |
| 蛋白名称 | Coilin |
| 蛋白大小 | 576 aa / 62.6 kDa |
| UniProt ID | P38432 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm, Nucleoli fibrillar center; UniProt: Nucleus; Nucleus, Cajal body |
| 蛋白大小 | 10/10 | ×1 | 10 | 576 aa / 62.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=14551 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024822, IPR031722, IPR056398; Pfam: PF15862, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm, Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Nucleus, Cajal body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14551 |
| PubMed broad count | 56651 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLN80 |

**关键文献**:
1. Coiled-Coil Design: Updated and Upgraded.. *Sub-cellular biochemistry*. PMID: 28101858
2. CCDC189 affects sperm flagellum formation by interacting with CABCOCO1.. *National science review*. PMID: 37601242
3. Design of Coiled-Coil Protein Nanostructures for Therapeutics and Drug Delivery.. *Annual review of chemical and biomolecular engineering*. PMID: 38598955
4. Coiled-Coil Protein Origami: Design, Isolation, and Characterization.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 37308636
5. Computational Prediction of Coiled-Coil Protein Gelation Dynamics and Structure.. *Biomacromolecules*. PMID: 38110299

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 57.5% |
| 有序区域 (pLDDT>70) 占比 | 32.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 32.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024822, IPR031722, IPR056398; Pfam: PF15862, PF23086 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOLC1 | 0.976 | 0.340 | — |
| SMN1 | 0.970 | 0.824 | — |
| FBL | 0.947 | 0.136 | — |
| ATXN1 | 0.912 | 0.591 | — |
| SNRPB | 0.911 | 0.610 | — |
| SART3 | 0.878 | 0.421 | — |
| WRAP53 | 0.829 | 0.292 | — |
| PSME3 | 0.815 | 0.694 | — |
| GEMIN2 | 0.806 | 0.093 | — |
| MPHOSPH10 | 0.804 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q95SB3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSP00000240316.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| htl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dip-B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| BYSL | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CEP76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CEP70 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CYB5R2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| DHX16 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| DNAJA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, Cajal body / Nuclear bodies; 额外: Nucleoplasm, Nucleoli fibrilla | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COIL — Coilin，研究基础较多，新颖性有限。
2. 蛋白大小576 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14551 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 14551 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P38432
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121058-COIL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COIL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P38432
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
