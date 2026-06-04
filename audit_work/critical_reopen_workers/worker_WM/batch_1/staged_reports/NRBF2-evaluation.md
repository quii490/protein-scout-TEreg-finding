---
type: protein-evaluation
gene: "NRBF2"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, accepted-on-reeval]
status: reevaluated
reeval_result: ACCEPT
original_rejection: "核定位得分 4/10 边缘 + 39 aa 蛋白过小 (误读)"
---

## NRBF2 -- RE-EVALUATED: ACCEPT (原始总分 133.5/180, 归一化 74.2/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRBF2 (COPR) |
| 蛋白名称 | Nuclear receptor-binding factor 2 |
| 蛋白大小 | 287 aa / 32.4 kDa |
| UniProt ID | Q96F24 |
| 核定位 (HPA IF) | Nucleoplasm, Cytosol (Approved) |
| 核定位 (UniProt) | Nucleus, Cytoplasm, Cytoplasmic vesicle, Autophagosome |
| 评估日期 | 2026-06-02 |
| 原始评估日期 | 2026-05 (approx) |
| 原始淘汰原因 | 核定位得分 4/10 边缘 + 蛋白大小 39 aa (数据误读) |

### 2. False Rejection Recheck

**原始淘汰判定**: 核定位得分 4/10 边缘 + 蛋白大小 39 aa 被判定为过小（实验困难）

**Recheck 发现**:

1. **蛋白大小数据错误**: UniProt 实际记录为 287 aa (32.4 kDa)，并非原始评估中的 39 aa。原始的蛋白大小数据存在严重的获取错误。287 aa 处于理想实验范围 (200-800 aa)，得分应为 10/10。

2. **核定位证据重新审视**: HPA IF 批准级证据指向 Nucleoplasm (主定位)，UniProt 也记录 Nucleus。GO-CC 含有 nucleoplasm (TAS:Reactome)。核定位证据来自三个独立数据库，互证充分。原始打分 4/10 偏低，应上调为 7/10。

3. **功能与 PI3KC3 自噬复合体的强关联**: NRBF2 是 PI3KC3 complex I (PI3KC3-C1) 的核心亚基，具有实验验证的蛋白互作 (BECN1, PIK3C3, ATG14, PIK3R4 等 combined score 0.999, experimental >0.99)。其功能涉及自噬调控、转录激活、神经祖细胞存活，与 TE 调控蛋白筛选的「染色质/转录调控+细胞稳态」目标高度吻合。

4. **文献新颖性优秀**: PubMed strict count = 33 篇 (≤40, 得分 8/10)。研究关注度适中，存在大量未探索空间。

**结论**: 原始淘汰系蛋白大小数据读取错误导致。修正后该基因在六大维度中表现良好，总分 133.5/180，推荐重新纳入候选名单。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm+ Cytosol (Approved); UniProt: Nucleus; GO nucleoplasm (TAS:Reactome) |
| 蛋白大小 | 10/10 | x1 | 10 | 287 aa / 32.4 kDa (理想范围 200-800 aa) |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=33 篇 (21-40 -> 8/10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=72.9, pct>90=41.5%; PDB: 4ZEY (X-ray 1.50A, 4-86 片段) |
| 调控结构域 | 6/10 | x2 | 12 | InterPro: IPR039679, IPR015056, IPR033393; Pfam: PF08961, PF17169 |
| PPI 网络 | 8/10 | x3 | 24 | STRING: BECN1/PIK3C3/ULK1/ATG14/RB1CC1/PIK3R4 (6个 partner score=0.999, 5个 experimental>0.99); IntAct 15 互作 |
| 互证加分 | -- | max +3 | 1.5 | PDB+AF (partial+predicted) + 多库定位一致 + STRING+IntAct 双源 |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus (ECO:0000250), Cytoplasm, Cytoplasmic vesicle, Autophagosome | Swiss-Prot |
| GO Cellular Component | nucleoplasm (GO:0005654, TAS:Reactome); autophagosome (GO:0005776); cytoplasm (GO:0005737, IDA:LIFEdb); cytoplasmic vesicle (GO:0031410); PI3K complex III (GO:0035032) | 多源证据 |

**核定位证据分析**:
- HPA IF Approved 级别可信度, Nucleoplasm 是主定位之一, 与 Cytosol 并列
- UniProt 标注 Nucleus (序列同源性推断, ECO:0000250), 同时标注 Cytoplasm 和 Autophagosome
- GO-CC nucleoplasm 注释来自 Reactome (TAS), 可靠
- 该蛋白在核-质之间穿梭的可能性高 (核受体结合因子功能)

**结论**: 三个数据库一致指向细胞核定位, 核定位特异性良好。原始评估低估了核定位证据。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 287 aa |
| 分子量 | 32.4 kDa |
| 理想范围 | 200-800 aa |

**评价**: 287 aa, 32.4 kDa 处于理想实验操作范围。适合常规克隆、表达、纯化及生化分析。原始评估中的 39 aa 为数据读取错误。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed symbol_only count | 42 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | COPR |

**关键文献**:
1. Wu MY, Liu L, Wang EJ et al. (2021). "PI3KC3 complex subunit NRBF2 is required for apoptotic cell clearance to restrict intestinal inflammation." *Autophagy*. PMID: 32160108
2. Zeng H, Chen H, Li M et al. (2021). "Autophagy protein NRBF2 attenuates endoplasmic reticulum stress-associated neuroinflammation and oxidative stress via promoting autophagosome maturation by interacting with Rab7 after SAH." *Journal of neuroinflammation*. PMID: 34530854
3. Foerster EG, Mukherjee T, Cabral-Fernandes L et al. (2022). "How autophagy controls the intestinal epithelial barrier." *Autophagy*. PMID: 33906557
4. Jin X, You L, Qiao J et al. (2024). "Autophagy in colitis-associated colon cancer: exploring its potential role in reducing initiation and preventing IBD-Related CAC development." *Autophagy*. PMID: 37723664
5. Qiu X, Li N, Yang Q et al. (2023). "The potent BECN2-ATG14 coiled-coil interaction is selectively critical for endolysosomal degradation of GPRASP1/GASP1-associated GPCRs." *Autophagy*. PMID: 37409929

**评价**: 33 篇文献，研究新颖性优秀。主要集中在自噬调控和炎症领域 (2021-2024)，上升趋势明显但仍有大量未探索空间。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 25.4% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 52.0% |
| 可用 PDB 条目 | 4ZEY (X-ray, 1.50A, 残基 4-86) |

**评价**: AlphaFold 预测质量中等偏上 (mean pLDDT=72.9), 约 52% 残基处于有序状态。PDB 4ZEY 为 1.50A 高分辨率晶体结构, 但仅覆盖 N 端 4-86 残基 (约 30% 全长)。总体结构可信度可接受，需要更多的全长实验结构。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR039679 (NRBF2 family), IPR015056, IPR033393 |
| Pfam | PF08961, PF17169 |

**染色质调控潜力分析**: NRBF2 含多个保守结构域，其中 NRBF2 家族结构域 (IPR039679) 与自噬 PI3KC3 复合体的组装和活性调控相关。虽然结构域功能尚未完全解析，但其在自噬体生物发生和 PI3KC3 脂激酶活性调控中的作用已通过功能实验验证 (PubMed:24785657, 25086043)。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BECN1 | 0.999 | 0.994 | 自噬核心 - Beclin 1 |
| PIK3C3 | 0.999 | 0.994 | PI3K 催化亚基 VPS34 |
| ULK1 | 0.999 | 0.994 | 自噬起始激酶 |
| ATG14 | 0.999 | 0.994 | PI3KC3 复合体亚基 |
| RB1CC1 | 0.999 | 0.994 | 自噬起始支架 FIP200 |
| PIK3R4 | 0.999 | 0.994 | PI3K 调控亚基 VPS15 |
| ATG101 | 0.962 | 0 | 自噬相关 |
| UVRAG | 0.943 | 0.095 | 自噬/内吞 |
| ULK2 | 0.942 | 0 | 自噬起始激酶 |
| BECN2 | 0.934 | 0.051 | Beclin 2 |

**实验验证互作** (IntAct, 精选):

| Partner | 方法 | PMID |
|---------|------|------|
| BECN1 | anti tag coimmunoprecipitation | 20562859 |
| PIK3C3 | anti tag coimmunoprecipitation | 20562859 |
| ULK1 | anti tag coimmunoprecipitation | 20562859 |
| ATG14 | anti tag coimmunoprecipitation | 20562859 |
| PIK3R4 | two hybrid array | 32296183 |
| KDM1A | two hybrid array | 32296183 |
| CDC23 | validated two hybrid | 32296183 |
| PRKAA1 | two hybrid | 20368287 |

**PPI 互证分析**:
- STRING+IntAct 均有强数据
- STRING partners: 15, IntAct interactions: 15
- 调控相关 (自噬/转录): 6/15 个 top partners 与自噬核心复合体直接相关
- PI3KC3 复合体中多个组分 (BECN1, PIK3C3, ATG14, PIK3R4) 均有 experimental >0.99

**评价**: PPI 网络非常出色。NRBF2 在自噬 PI3KC3 复合体中的多个核心伙伴均具有高置信度实验互作证据, 提示其在细胞稳态调控中的关键地位。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB 4ZEY | pLDDT=72.9, v6, 1 PDB 片段 | 预测+实验 (部分) |
| 定位 | UniProt + HPA + GO | Nucleus / Nucleoplasm+Cytosol / nucleoplasm | 一致 (核定位) |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证 (partial crystal + full prediction): +0.5
- 多库定位一致 (UniProt + HPA + GO-CC, 3源核定位): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 5. 总体评价

**推荐等级**: ACCEPT (原始评估 REJECTED -> 重新评估 ACCEPT)

**核心优势**:
1. NRBF2 是 PI3KC3 自噬复合体的核心组分, 拥有 6 个 experimental=0.994 的 STRING 互作伙伴 (BECN1, PIK3C3, ULK1, ATG14, RB1CC1, PIK3R4), PPI 网络极强
2. 287 aa, 32.4 kDa 为理想实验大小
3. PubMed 仅 33 篇, 新颖性优秀, 存在大量未探索空间
4. 核定位有 HPA Approved + UniProt + GO-CC 三源互证
5. 涉及自噬、神经炎症、氧化应激和肠道免疫等多个新兴方向

**风险/不确定性**:
1. 蛋白功能主要通过序列同源性推断 (By similarity), 直接实验证据有限 (但 PPI 实验证据充分)
2. AlphaFold 预测仅有 52% 有序区域, PDB 仅覆盖 N 端 30%
3. 该蛋白在核-质间穿梭, 核内具体功能 (如转录调控) 尚未充分阐明, 可能需要通过 ChIP-seq / RNA-seq 等方法验证

**False Rejection 定性**:
原始淘汰系蛋白大小数据读取错误 (287 aa 误作 39 aa), 且核定位证据被低估。修正后各项指标表现良好, 核定位证据充分, 蛋白大小理想, 研究新颖性优秀, PPI 网络突出。

**下一步建议**:
- [ ] 确认 NRBF2 在目标 TE 调控实验体系中的表达水平
- [ ] 设计 Co-IP 实验验证 NRBF2 与 PI3KC3 复合体在核内的互作
- [ ] 通过 IF 验证核定位并评估核-质分布比例
- [ ] 考虑以 NRBF2 为切入点研究自噬与核内转录调控的交叉

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F24
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148572-NRBF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRBF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F24
- STRING: https://string-db.org/network/9606.ENSP00000277746
- Data fetched live: 2026-06-02
