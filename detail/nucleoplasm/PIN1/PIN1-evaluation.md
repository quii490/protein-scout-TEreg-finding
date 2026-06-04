---
type: protein-evaluation
gene: "Pin1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Pin1 — REJECTED (研究热度过高 (PubMed strict=1392，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Pin1 |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase NIMA-interacting 1 |
| 蛋白大小 | 163 aa / 18.2 kDa |
| UniProt ID | Q13526 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 163 aa / 18.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1392 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.6; PDB: 1F8A, 1I6C, 1I8G, 1I8H, 1NMV, 1NMW, 1PIN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046357, IPR051370, IPR000297, IPR023058, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- midbody (GO:0030496)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1392 |
| PubMed broad count | 2385 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Stabilization of Pin1 by USP34 promotes Ubc9 isomerization and protein sumoylation in glioma stem cells.. *Nature communications*. PMID: 38167292
2. PIN1 and CDK1 cooperatively govern pVHL stability and suppressive functions.. *Cell death and differentiation*. PMID: 36813923
3. Reciprocal antagonism of PIN1-APC/C(CDH1) governs mitotic protein stability and cell cycle entry.. *Nature communications*. PMID: 38622115
4. Pin1-Catalyzed Conformation Changes Regulate Protein Ubiquitination and Degradation.. *Cells*. PMID: 38727267
5. Sumoylation of methionine adenosyltransferase alpha 1 promotes mitochondrial dysfunction in alcohol-associated liver disease.. *Hepatology (Baltimore, Md.)*. PMID: 38100286

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 85.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 1F8A, 1I6C, 1I8G, 1I8H, 1NMV, 1NMW, 1PIN, 1ZCN, 2F21, 2ITK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1F8A, 1I6C, 1I8G, 1I8H, 1NMV, 1NMW, 1PIN, 1ZCN, 2F21, 2ITK）+ AlphaFold极高置信度预测（pLDDT=91.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046357, IPR051370, IPR000297, IPR023058, IPR001202; Pfam: PF00639, PF00397 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRF3 | 0.967 | 0.300 | — |
| HIPK2 | 0.965 | 0.314 | — |
| TP53 | 0.946 | 0.750 | — |
| POLR2A | 0.912 | 0.858 | — |
| SFN | 0.909 | 0.900 | — |
| MYC | 0.881 | 0.714 | — |
| PML | 0.836 | 0.787 | — |
| PLK1 | 0.821 | 0.625 | — |
| NCF1 | 0.800 | 0.000 | — |
| NCF4 | 0.800 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBBP8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NONO | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAI1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GGA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZMIZ2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HNRNPC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSC22D4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 1F8A, 1I6C, 1I8G, 1I8H, 1NMV,  | pLDDT=91.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. Pin1 — Peptidyl-prolyl cis-trans isomerase NIMA-interacting 1，研究基础较多，新颖性有限。
2. 蛋白大小163 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1392 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1392 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13526
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127445-PIN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Pin1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13526
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
