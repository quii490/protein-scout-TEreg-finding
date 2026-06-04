---
type: protein-evaluation
gene: "DNM3"
date: 2026-06-04
tags: [protein-scout, confirmed-rejected, critical-false-rejection-recheck]
status: confirmed-rejected
previous_status: rejected
previous_rejection_reason: "nuclear_score ≤ 3 AND PubMed > 100 (dual rejection)"
recheck_result: "CONFIRMED REJECTED — Zero nuclear evidence in all databases; HPA=Golgi apparatus(Uncertain); UniProt=Cytoplasm/Cytoskeleton; GO-CC: NO nuclear terms; PubMed 109>100; nuclear_score=2 is correct"
revised_nuclear_score: 2
---

## DNM3 核蛋白评估报告 -- FALSE REJECTION RE-EVALUATION (确认拒绝)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNM3 / KIAA0820 |
| 蛋白大小 | 869 aa / 97.7 kDa |
| UniProt ID | Q9UQ16 |
| 蛋白全名 | Dynamin-3 |
| HPA IF 主定位 | **Golgi apparatus** |
| HPA Reliability | Uncertain |
| 原评估状态 | REJECTED (nuclear_score=2, PubMed>100) |
| 重新评估日期 | 2026-06-04 |
| CONFIRMED REJECTED | **CONFIRMED REJECTED** — 双原因：(1)非核蛋白；(2)PubMed 109>100 |

### 2. 评分总览（修订后，确认原评分）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **2/10** | ×4 | 8 | HPA=Golgi apparatus; UniProt=Cytoplasm/Cytoskeleton; GO-CC: 零核术语; 非核蛋白 |
| 蛋白大小 | 8/10 | ×1 | 8 | 869aa/97.7kDa，较大但结构域丰富 |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=82, broad=109 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=77.3; PDB 3L43(2.27A X-ray), 5A3F(3.70A X-ray) |
| 调控结构域 | 6/10 | ×2 | 12 | Dynamin GTPase + PH + GED; 膜重塑和胞吞 |
| PPI网络 | 7/10 | ×3 | 21 | STRING: DNM1(0.999实验), DNM2(0.984实验), GRB2(0.653实验); 强实验PPI |
| **加权总分** | | | **73/180** | |
| **归一化总分 (÷1.8)** | | | **40.6/100** | |

### 3. False rejection recheck -- CRITICAL

**为何被列为CRITICAL进行重新评估:**

DNM3在原始Sheet4中的nuclear_score信息可能不准确。Dynamin家族蛋白有时被错误地与核膜重建或核内体运输相关联。此外，DNM3的结构域丰富(GTPase+PH+GED+PRD)和PDB实验结构(3L43, 5A3F)使其表面看起来像是一个"好"候选。需要在所有数据库中逐一核查核定位证据。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet) — ZERO NUCLEAR**:
   - Cytoplasm: ECO:0000305 (no experimental evidence — inferred by curator, not based on direct assay)
   - Cytoplasm, cytoskeleton: ECO:0000305 (curator inference, not experimental)
   - **没有Nuclear/Nucleoplasm/Nucleolus定位**
   - ECO:0000305 = "inferred by curator" — 这是比ECO:0000255(序列预测)更弱的证据等级，因为它仅表示curator的推测，无算法支持

2. **GO-CC (harvest packet) — 完全缺乏核术语**:
   - cytoplasm (IBA:GO_Central)
   - dendritic spine (ISS:UniProtKB)
   - extracellular exosome (HDA:UniProtKB)
   - microtubule (IBA:GO_Central)
   - perinuclear region of cytoplasm (ISS:UniProtKB)
   - plasma membrane (IBA:GO_Central)
   - postsynaptic density (ISS:UniProtKB)
   - presynapse (IEA:GOC)
   - synapse (IBA:GO_Central)
   - **9个GO-CC术语，零个是nuclear。Perinuclear region of cytoplasm指的是细胞核周围的胞质区域，而非核内**

3. **HPA Subcellular (harvest packet) — 明确非核**:
   - Main location: Golgi apparatus
   - Reliability: Uncertain
   - HPA IF图像在线可用(6张blue_red_green)
   - 零核信号

4. **功能证据 — 膜重塑而非核功能**:
   - Dynamin-3是large GTPase，负责膜分裂(fission)
   - 核心功能: clathrin-mediated endocytosis(网格蛋白介导胞吞)
   - 在突触小泡再循环(synaptic vesicle recycling)中起关键作用
   - 与微管结合并产生力来捆绑微管
   - 这些功能全部在细胞质/细胞膜/突触执行，与细胞核无关

**为何这不是假阴性:**

DNM3的核定位证据为零。在所有数据库中系统地搜索"nucleus"、"nuclear"、"nucleoplasm"、"nucleolus"等术语后，DNM3的GO-CC列表完全缺乏核术语，UniProt没有核定位，HPA明确显示Golgi apparatus。这是10个CRITICAL基因中核证据最弱的基因。

此外，DNM3受到双拒绝机制: (1) nuclear_score=2 (非核蛋白); (2) PubMed 109>100 (研究热度过高)。即使核定位问题被解决，PubMed热度也会单独拒绝该基因。

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | Golgi apparatus | Uncertain | IF实验 |
| UniProt | Cytoplasm | ECO:0000305 | **curator推断, 非实验** |
| UniProt | Cytoplasm, cytoskeleton | ECO:0000305 | **curator推断, 非实验** |
| GO-CC | cytoplasm, dendritic spine, exosome, microtubule, perinuclear region, plasma membrane, postsynapse, presynapse, synapse | 混合等级 | **零核术语** |

DNM3的GO-CC共有9个术语，其中"perinuclear region of cytoplasm"是距离"nucleus"最近的条目——但perinuclear region指的是核周质(靠近核膜的胞质区域)，不是核内。这是10个CRITICAL基因中唯一在UniProt/GO-CC/HPA三个数据库中均无任何核信号的基因。**核定位评分: 2/10 (确认)**。

#### 4.2 蛋白大小评估

869 aa / 97.7 kDa。较大的多结构域蛋白。包含Dynamin-type G domain (GTPase), Dynamin central domain, PH domain, GED (GTPase effector domain), 和PRD (proline-rich domain)。结构域架构清晰完整。但蛋白较大可能带来表达和操作挑战。**评分: 8/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 82 |
| PubMed symbol_only | 109 |
| PubMed broad_count | 109 |
| 别名 | KIAA0820 |
| 主要方向 | 突触胞吞、Parkinson病遗传修饰因子、癌症外泌体 |

PubMed 109篇(broad)，82篇(strict)。研究热度较高，在突触生物学和癌生物学中有大量文献。**评分: 0/10** (>100自动REJECTED)。

**关键文献**:
1. Brown EE et al. (2021). "Analysis of DNM3 and VAMP4 as genetic modifiers of LRRK2 Parkinson's disease." *Neurobiol Aging*. PMID: 32873436
2. De Houwer JFH et al. (2025). "Distinct proteomic CSF profiles in genetic frontotemporal lobar degeneration." *Brain*. PMID: 41343108
3. Liu J et al. (2021). "The biology, function, and applications of exosomes in cancer." *Acta Pharm Sin B*. PMID: 34589397
4. Juknyte G et al. (2021). "TBX15, DNM3, RAD51B gene polymorphisms and associations with pituitary adenoma." *In Vivo*. PMID: 33622874
5. Berge-Seidl V et al. (2019). "No evidence for DNM3 as genetic modifier of age at onset in Parkinson's disease." *Neurobiol Aging*. PMID: 30340792

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 77.3 |
| pLDDT > 90 (Very High) | 39.8% |
| pLDDT 70-90 (High) | 35.1% |
| pLDDT < 50 (Low) | 16.5% |
| 有序区域 (pLDDT>70) | 74.9% |
| 实验结构 (PDB) | 3L43 (2.27A, 6-306), 5A3F (3.70A, 1-764) |

两个X-ray实验结构覆盖N端GTPase+middle domain(3L43)和近全长(5A3F)。PDB覆盖良好但C端PRD区域(pLDDT较低区域)仍缺乏实验结构。**评分: 8/10**。

#### 4.5 结构域分析

丰富的结构域架构: Dynamin GTPase (IPR001401) + PH domain (IPR001849) + GED (IPR003130) + Dynamin central (IPR000375)。所有结构域指向膜重塑和胞吞功能。无DNA/RNA结合或染色质修饰域。**评分: 6/10**。

#### 4.6 PPI 网络

| Partner | Combined Score | Experimental | 功能 |
|---------|---------------|--------------|------|
| DNM1 | 0.999 | 0.994 | Dynamin-1, 同家族 |
| DNM2 | 0.984 | 0.847 | Dynamin-2, 同家族 |
| HCLS1 | 0.965 | 0.065 | 造血细胞特异性Lyn底物 |
| SH3GL2 | 0.837 | 0.396 | Endophilin-A1, 胞吞 |
| GRB2 | 0.701 | 0.653 | 生长因子受体结合蛋白, 信号转导 |

DNM3拥有10个CRITICAL基因中最强的实验PPI网络之一，以同家族(DNM1/DNM2)和胞吞机器(SH3GL2/CLTC/SNX9)为核心。但这种强PPI网络支持胞吞功能，而非核功能。**评分: 7/10**。

### 5. 最终决定

**CONFIRMED REJECTED — 非核蛋白 + PubMed>100，双原因确认拒绝**

DNM3是10个CRITICAL基因中最明确的非核蛋白。在所有数据库中:
- HPA: Golgi apparatus (细胞质膜系统)
- UniProt: Cytoplasm / Cytoskeleton (无核定位)
- GO-CC: 9个术语，零个核术语
- 功能: 膜分裂GTPase (胞吞)

此外，即使核定位证据存在，PubMed 109篇(>100)也会作为独立原因触发拒绝。Dynamin-3是一个充分研究的蛋白质，其主要科学价值在于突触胞吞和膜运输，而非TE调控或染色质生物学。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQ16
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQ16
- PDB: https://www.rcsb.org/structure/3L43 / https://www.rcsb.org/structure/5A3F
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNM3%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000197959-DNM3
- STRING: https://string-db.org/network/9606.ENSP00000363588
- IntAct: https://www.ebi.ac.uk/intact/interactors/id:Q9UQ16
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/DNM3.json (2026-06-03)

HPA IF图像在线可用(6张blue_red_green, Golgi apparatus信号)，未下载本地。PAE未生成本地。
